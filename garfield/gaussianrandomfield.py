import numpy as np
from fourier   import large_scale_ix
from scipy.fft import rfftn, irfftn

def generate(mu, sigma, shape, rng):
    grf = rng.normal(mu, sigma, shape)
    print('GRF :', grf.dtype, grf.shape)
    return grf

def decrease_resolution(grf_hr, shape_lr):
    # Real-to-complex forward FFT high-res GRF
    fft_hr = rfftn(grf_hr)
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
    print('GRF lr transformed:', fft_lr.dtype, fft_lr.shape)

    # Complex-to-real inverse FFT low-res GRF
    grf_lr = irfftn(fft_lr, overwrite_x=True)
    print('GRF lr            :', grf_lr.dtype , grf_lr.shape)
    
    return grf_lr

def increase_resolution(grf_lr, shape_hr, rng):
    # High-res GRF with same mean and variance
    mu     = np.mean(grf_lr.ravel())
    sigma  = np.std( grf_lr.ravel())
    grf_hr = generate(mu, sigma, shape_hr, rng)
    fft_hr = rfftn(grf_hr)
    
    # Real-to-complex forward FFT low-res GRF
    fft_lr = rfftn(grf_lr)
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
    print('GRF hr transformed:', fft_hr.dtype, fft_hr.shape)

    # Complex-to-real inverse FFT high-res GRF
    grf_hr = irfftn(fft_hr, overwrite_x=True)
    print('GRF hr            :', grf_hr.dtype, grf_hr.shape)
    
    return grf_hr
