# GaRField

GaRField generates Gaussian Random Fields in arbitrary dimensions with consistent multi-resolution realizations. Low-frequency Fourier modes of the original field are preserved, allowing simulations at multiple resolutions without modifying the large-scale structure. This makes the package suitable for astrophysics, cosmology, physics, and any application requiring controlled multi-resolution stochastic fields.

# Modules

## gaussianrandomfield

`generate` produces a GRF with a specified mean and sigma and returns an N-dimensional array.

`decrease_resolution` extracts the large-scale Fourier modes from an input GRF and returns a lower-resolution array.

`increase_resolution` combines the input GRF with additional small-scale modes and returns a higher-resolution array.

# Notebooks

`garfield_basic.ipynb` generates a GRF and saves the ND array as a `.npy` file.

`garfield_decrease_resolution.ipynb` extracts the large-scale Fourier modes from a base GRF to produce a lower-resolution version.

`garfield_increase_resolution.ipynb` combines the large-scale Fourier modes from the base GRF with additional smaller-scale modes from a higher-resolution realization.
