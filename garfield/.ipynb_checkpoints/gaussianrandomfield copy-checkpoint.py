import numpy as np
from scipy.fft import rfftn, irfftn

def make(mu, sigma, dim, rng):
    grf = rng.normal(mu, sigma, dim)
    print('GRF :', grf.dtype, grf.shape)
    return grf

def mask_fft(dim_small, dim_large):
    # Slice rules per dimension
    print(dim_small, np.prod(dim_small))
    print(dim_large, np.prod(dim_large))
    slice_rules        = np.empty((len(dim_small),2), dtype=int)
    slice_rules[:-1,0] =  dim_small[:-1]//2 + 1
    slice_rules[:-1,1] = dim_large[:-1] -dim_small[:-1]//2
    slice_rules[ -1,:] = (dim_small[-1],dim_large[-1])
    print(slice_rules)

    # Array slices
    slices = tuple(slice(*rule) if rule is not None else slice(None) for rule in slice_rules)
    print(slices)

    # Mask
    mask         = np.ones(dim_large, dtype=bool)
    mask[slices] = False
    print("Mask :", mask.dtype, mask.shape, np.sum(mask), np.sum(mask == False))
    
    return mask

def expand(grf1, grf2):
    # Real-to-complex forward FFT
    grf1t = rfftn(grf1)
    
    # Replace with large-scale modes from grf1
    mask       = mask_fft(grf1.shape, grf2.shape)
    grf2[mask] = grf1

    return grf2

def reduce(grf1, grf2_dim):
    # Real-to-complex forward FFT
    grf1t = rfftn(grf1)
    print('GRF1            :', grf1.dtype , grf1.shape )
    print('GRF1 transformed:', grf1t.dtype, grf1t.shape)

    # Mask for low-frequency modes
    dim_large     = grf1t.shape
    dim_small     = grf2_dim
    dim_small[-1] = dim_small[-1]//2 + 1
    mask          = mask_fft(dim_small, dim_large)
        
    # Copy low-frequency modes from grf1
    grf2t = grf1t[mask] #.reshape(dim_small)
    print('GRF2 transformed:', grf2t.dtype, grf2t.shape)

    # Complex-to-real inverse FFT
    grf2 = irfftn(grf2t, overwrite_x=True)
    print('GRF2            :', grf2.dtype , grf2.shape)
    
    return grf2