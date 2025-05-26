# Urban_landuse_pune
This project demonstrates a basic GIS and remote sensing workflow using Python. It includes a dummy raster land cover dataset, sample coordinate data, and a simple classification visualization script.

## Project Structure
- urban_classification.py - Python script to visualize and summarize the classified land cover raster.
- pune_landcover.tif - Simulated GeoTIFF raster with 3 land cover classes (Urban, Vegetation, Water).
- sample_coordinates.csv - Sample latitude-longitude points labeled with land cover classes.

## Tools Used
- Python
- Rasterio
- NumPy
- Matplotlib
- CSV and TIFF file handling

## Description
The project creates a dummy raster representing land cover types in a simplified Pune region context. The raster contains three classes:
- `0` - Urban
- `1` - Vegetation
- `2` - Water

The script visualizes the raster and prints pixel count statistics for each class.

##  How to Run
1. Clone this repository or download the files.
2. Ensure you have the required Python packages (`rasterio`, `matplotlib`, `numpy`).
3. Run the script using:

```bash
python urban_classification.py
```

## Sample Output
- A plot of the land cover map using a terrain colormap.
- Console output showing the number of pixels in each class.

This is a sample educational project to demonstrate Python and GIS integration. You can replace the dummy data with real satellite data and classification results.

