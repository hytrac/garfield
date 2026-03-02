import numpy as np

def make(dim, rng):
    mu    = 0.0 # zero mean
    sigma = 1.0 # unit variance
    return rng.normal(mu, sigma, size = dim)


def input(file):
    print("Loading ",file)
    return np.load(file)


def outputfile, grf):
    print("Saving ",file)
    return np.save(file, grf)    


def expand(grf1, dim2):
    # Init
    grf2 = np.zeros(dim2)
    
    return grf2


def reduce(grf1, dim2):
    # Init
    grf2 = np.zeros(dim2)
    
    return grf2