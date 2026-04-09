import numpy as np
from scipy.fft import rfftn, irfftn

def generate(mu, sigma, shape, rng, verbose=False):
    """
    Generate a Gaussian random field.

    Parameters
    ----------
    mu : float
        Mean of the Gaussian distribution.
    sigma : float
        Standard deviation of the Gaussian distribution.
    shape : tuple of int
        Shape of the output array.
    rng : numpy.random.Generator
        Random number generator used to draw the samples.
    verbose : bool, optional
        If True, print diagnostic information (default is False).

    Returns
    -------
    ndarray
        Array of Gaussian random numbers with the specified mean,
        standard deviation, and shape.
    """
    
    # Draw random samples from a normal (Gaussian) distribution
    grf = rng.normal(mu, sigma, shape)

    if (verbose):
        print('GRF :', grf.dtype, grf.shape)
        
    return grf

def decrease_resolution(grf_hr, shape_lr, verbose=False):
    """
    Downsample a high-resolution Gaussian random field by keeping only
    large-scale (low-frequency) Fourier modes.

    Parameters
    ----------
    grf_hr : ndarray
        High-resolution real-space field.
    shape_lr : tuple of int
        Desired shape of the low-resolution field.
    verbose : bool, optional
        If True, print diagnostic information (default is False).

    Returns
    -------
    ndarray
        Low-resolution real-space field.
    """
    
    # Real-to-complex forward FFT high-res GRF
    fft_hr = rfftn(grf_hr)

    if (verbose):
        print('GRF hr            :', grf_hr.dtype, grf_hr.shape)
        print('GRF hr transformed:', fft_hr.dtype, fft_hr.shape)

    # Indices for large-scale/low-frequency modes
    shape     = np.copy(shape_lr)
    shape[-1] = shape[-1]//2 + 1
    indices   = large_scale_ix(shape)
        
    # Copy large-scale modes, scale amplitudes, and keep dc mode
    dc    = (0,)*fft_hr.ndim
    scale = np.prod(shape_lr)/np.prod(grf_hr.shape)
    fft_lr     = fft_hr[indices]*np.sqrt(scale)
    fft_lr[dc] = fft_hr[dc]*scale

    if (verbose):
        print('GRF lr transformed:', fft_lr.dtype, fft_lr.shape)
    
    # Complex-to-real inverse FFT low-res GRF
    grf_lr = irfftn(fft_lr, overwrite_x=True)

    if (verbose):
        print('GRF lr            :', grf_lr.dtype , grf_lr.shape)
    
    return grf_lr

def increase_resolution(grf_lr, shape_hr, rng, verbose=False):
    """
    Upsample a low-resolution Gaussian random field by embedding 
    its large-scale Fourier modes into a higher-resolution field.

    Parameters
    ----------
    grf_lr : ndarray
        Low-resolution real-space field.
    shape_hr : tuple of int
        Desired shape of the high-resolution field.
    rng : numpy.random.Generator
        Random number generator used to generate small-scale fluctuations.
    verbose : bool, optional
        If True, print diagnostic information (default is False).

    Returns
    -------
    ndarray
        High-resolution real-space field.
    """
    
    # High-res GRF with same mean and variance
    mu     = np.mean(grf_lr.ravel())
    sigma  = np.std( grf_lr.ravel())
    grf_hr = generate(mu, sigma, shape_hr, rng)
    fft_hr = rfftn(grf_hr)
    
    # Real-to-complex forward FFT low-res GRF
    fft_lr = rfftn(grf_lr)

    if (verbose):
        print('GRF lr            :', grf_lr.dtype, grf_lr.shape)
        print('GRF lr transformed:', fft_lr.dtype, fft_lr.shape)
    
    # Indices for large-scale modes
    shape   = np.copy(fft_lr.shape)
    indices = large_scale_ix(shape)
    
    # Replace large-scale modes, scale amplitudes, and keep dc mode
    dc    = (0,)*fft_lr.ndim
    scale = np.prod(shape_hr)/np.prod(grf_lr.shape)
    fft_hr[indices] = fft_lr*np.sqrt(scale)
    fft_hr[dc]      = fft_lr[dc]*scale

    if (verbose):
        print('GRF hr transformed:', fft_hr.dtype, fft_hr.shape)
    
    # Complex-to-real inverse FFT high-res GRF
    grf_hr = irfftn(fft_hr, overwrite_x=True)

    if (verbose):
        print('GRF hr            :', grf_hr.dtype, grf_hr.shape)
    
    return grf_hr

def smooth_field(grf, window_func, box=1.0):
    # Real-to-complex forward FFT
    field = rfftn(grf)

    # Complex-to-real inverse FFT smoothed GRF
    grf_sm = irfftn(field, overwrite_x=True)
    
    return grf_sm

def large_scale_ix(small_shape):
    """
    Generate an index tuple for selecting large-scale (low-frequency) Fourier modes.

    Parameters
    ----------
    small_shape : tuple of int
        Shape of the smaller grid along each axis.

    Returns
    -------
    tuple of ndarray
        Tuple of index arrays suitable for `np.ix_`.
    """
    
    # Number of dimensions
    ndim = len(small_shape)
    
    # Build index arrays per axis
    indices = []
    for ax, nk in enumerate(small_shape):
        if ax < ndim - 1:
            half = nk//2
            indices.append(np.roll(np.arange(-half,half),half))
        else:
            indices.append(np.arange(nk))
    
    return np.ix_(*indices)