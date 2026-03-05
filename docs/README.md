# GaRField

GaRField generates Gaussian Random Fields in arbitrary dimensions with consistent multi-resolution realizations. Low-frequency Fourier modes of the original field are preserved, allowing simulations at multiple resolutions without modifying the large-scale structure. This makes the package suitable for astrophysics, cosmology, physics, and any application requiring controlled multi-resolution stochastic fields.

# Notebooks

`garfield_basic.ipynb`: generate a GRF and save as a numpy file.

`garfield_decrease_resolution.ipynb`: First generate/read a main GRF, then decrease the resolution, and save the lower-resolution array as a numpy file.

`garfield_increase_resolution.ipynb`: First generate/read a main GRF, then increase the resolution, and save the higher-resolution array as a numpy file.


