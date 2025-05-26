
import rasterio
import numpy as np
import matplotlib.pyplot as plt

# Load raster data
with rasterio.open("pune_landcover.tif") as src:
    band = src.read(1)
    plt.imshow(band, cmap='terrain')
    plt.title("Urban Land Cover Classification")
    plt.colorbar(label='Class')
    plt.show()

# Simple stats
unique, counts = np.unique(band, return_counts=True)
for u, c in zip(unique, counts):
    print(f"Class {u}: {c} pixels")
