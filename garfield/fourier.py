import numpy as np

def large_scale_ix(small_shape):
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