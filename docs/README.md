# GaRField

GaRField generates Gaussian Random Fields in arbitrary dimensions with consistent multi-resolution realizations. Low-frequency Fourier modes of the original field are preserved, allowing simulations at multiple resolutions without modifying the large-scale structure. This makes the package suitable for astrophysics, cosmology, physics, and any application requiring controlled multi-resolution stochastic fields.

# Notebooks

`garfield_basic.ipynb`
- generate a GRF
- save the ND array as a numpy file

<br>

`garfield_decrease_resolution.ipynb`
- generate a base GRF or read data from a file
- decrease the resolution
- save the lower-resolution array as a numpy file

<br>

`garfield_increase_resolution.ipynb`
- generate a base GRF or read data from a file
- increase the resolution
- save the higher-resolution array as a numpy file




