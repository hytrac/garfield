# GaRField

GaRField generates Gaussian Random Fields in arbitrary dimensions with consistent multi-resolution realizations. Low-frequency Fourier modes of the original field are preserved, allowing simulations at multiple resolutions without modifying the large-scale structure. This makes the package suitable for astrophysics, cosmology, physics, and any application requiring controlled multi-resolution stochastic fields.

# Notebooks

`garfield_basic.ipynb`
- Generate a GRF with a specified Gaussian mean, Gaussian sigma, and N-dimensional array shape
- Save the resulting array as a `.npy` file

<br>

`garfield_decrease_resolution.ipynb`
- Generate a base GRF or read data from a file
- Decrease the resolution while preserving the large-scale Fourier modes of the base GRF
- Save the lower-resolution array as a `.npy` file

<br>

`garfield_increase_resolution.ipynb`
- Generate a base GRF or read data from a file
- Combine the large-scale modes from the base GRF with additional smaller-scale modes from a higher-resolution realization
- Save the higher-resolution array as a `.npy` file

