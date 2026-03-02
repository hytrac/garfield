import numpy as np

def load(file):
    print("Load ", file)
    return np.load(file)

def save(file, data):
    print("Save ", file)
    return np.save(file, data)
    