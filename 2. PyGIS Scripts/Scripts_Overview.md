# QGIS & Python Geospatial Property Analysis

## Overview

This repository demonstrates how to map, analyze, and visualize property data using **QGIS** and Python, with an emphasis on reproducible workflows for machine learning and spatial analysis. The project is built on a dataset of roughly 60,000 properties—including geospatial and attribute information—and a set of PyQGIS scripts for automating every major step of the mapping and analysis process.

---

## Background

Modern geospatial projects often require seamless integration of attribute-rich datasets with mapping tools and machine learning. By leveraging QGIS and PyQGIS, this project enables:

- **Automated spatial visualization**: Map thousands of property records efficiently.
- **Analytical workflows**: Filter, classify, and flag properties based on key attributes (like tax compliance).
- **Preparation for machine learning**: Structure and export enriched spatial datasets for further analysis and prediction tasks.

---

## Dataset Description

The main dataset contains property data with detailed columns as follows:

| Column Name         | Description                                                      |
|---------------------|------------------------------------------------------------------|
| `Property_ID`       | Unique property identifier                                       |
| `Cluster_Type`      | Type of neighborhood/cluster                                     |
| `Address`           | Full postal address                                              |
| `Property_Type`     | Residential, Commercial, etc.                                    |
| `Floors`            | Structure in floors (e.g., G+2)                                  |
| `Construction_Type` | Building material (e.g., RCC, Load Bearing)                      |
| `Plot_Area`         | Area in square units                                             |
| `Latitude`          | Geographic latitude (WGS84)                                      |
| `Longitude`         | Geographic longitude (WGS84)                                     |
| `Electricity_ID`    | Associated electricity identifier                                |
| `Year_Built`        | Year of construction                                             |
| `Tax_Compliance`    | If property tax compliant (True/False)                           |


---

## Scripts & Workflow

Run the scripts in the following order after opening a new QGIS project:

1. **Importing_OSM_Layer.py**  
   Loads OpenStreetMap as a basemap to provide geographic context.

2. **Importing_Points.py**  
   Imports all property points from the main CSV as a spatial layer.

3. **Importing_Typewise.py**  
   Styles each property point by `Property_Type` (e.g., red for residential, yellow for commercial).

4. **Flagging_Unpaid.py**  
   Adds a point layer for properties where `Tax_Compliance` is `False` (defaulters).

5. **Unpaid_Heatmap.py**  
   Creates a heatmap layer indicating the density of tax-defaulters.

6. **Saving_Heatmap.py**  
   Saves the heatmap as a raster `.tif` file for future use.

7. **Converting_Files_For_Cloud.py**  
   Converts all layers to `GeoJSON` or `GPKG` for cloud compatibility and sharing.

---

#### NOTE : Run all the scripts only on PyGIS (python codewriter in QGIS). Also, first make sure it is intalled as plugin.