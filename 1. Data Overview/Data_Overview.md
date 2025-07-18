# 🗂️ Data Overview & Background

## 📘 Background

This project is based on a rich dataset of approximately **60,000 individual properties**, curated for geospatial analysis and machine learning tasks in a QGIS-Python (PyQGIS) environment. The information includes geolocation data (latitude and longitude), property attributes (type, floors, construction, area), and fiscal compliance indicators (e.g., tax compliance).

The aim is to build tools that allow seamless:

- 🗺️ Visualization of property distributions on a map using QGIS.
- 📊 Attribute-based and spatial filtering (e.g., residential properties built before 2000).
- 🤖 Integration with machine learning models to analyze spatial trends or predict tax compliance.
- 🔁 Reproducible and automated GIS workflows via Python scripting.

This dataset serves as the foundational layer for all spatial and predictive modeling conducted in this repository.

---

## 🧾 Dataset Schema

Each record in the dataset corresponds to one property. The data is stored in a CSV file and includes the following structured fields:

| Column Name         | Description                                                       |
|---------------------|-------------------------------------------------------------------|
| `Property_ID`       | Unique identifier for each property                               |
| `Cluster_Type`      | Cluster classification (e.g., Residential, Commercial Block)      |
| `Address`           | Full postal address of the property                               |
| `Property_Type`     | General classification like Residential or Commercial             |
| `Floors`            | Construction structure in floor format (e.g., G+1, G+4)           |
| `Construction_Type` | Type of construction (e.g., RCC, Load Bearing)                    |
| `Plot_Area`         | Area of the property in square units (e.g., sq meters or feet)    |
| `Latitude`          | GPS latitude coordinate in WGS84 projection                       |
| `Longitude`         | GPS longitude coordinate in WGS84 projection                      |
| `Electricity_ID`    | Utility-related identifier for cross-referencing                  |
| `Year_Built`        | Year when the property was constructed                            |
| `Tax_Compliance`    | Boolean (True/False) indicating current tax compliance status     |

---

## 🔍 Sample Records

Here’s a preview of the dataset (first 5 rows):

| Property_ID | Cluster_Type | Address                      | Property_Type | Floors | Construction_Type | Plot_Area | Latitude   | Longitude   | Electricity_ID | Year_Built | Tax_Compliance |
|-------------|--------------|------------------------------|---------------|--------|-------------------|-----------|------------|-------------|----------------|------------|----------------|
| DL-100000   | Residential  | 630 Miller Place             | Residential   | G+2    | RCC               | 371.92    | 28.593553  | 77.072279   | 3031824858     | 1992.0     | True           |
| DL-100001   | Residential  | 43828 Brennan Motorway       | Residential   | G+1    | Load Bearing      | 972.69    | 28.546182  | 77.016234   | 3208033559     | 2012.0     | True           |
| DL-100002   | Residential  | 33109 Cantrell Sq Apt. 664   | Residential   | G+2    | Load Bearing      | 839.79    | 28.617673  | 77.031393   | 3323384309     | 2008.0     | True           |
| DL-100003   | Residential  | 97528 Gary Avenue Suite 973  | Residential   | G+4    | RCC               | 143.47    | 28.584711  | 77.063754   | 3395431722     | 2012.0     | True           |
| DL-100004   | Residential  | 8373 Melissa Trace           | Residential   | G+1    | Load Bearing      | 474.15    | 28.564447  | 77.070118   | 3259146589     | 1989.0     | True           |

---

## 🧠 Use Cases

This data serves as a launchpad for multiple geospatial and machine learning workflows, including:

- Clustering properties based on location and attributes
- Spatial-temporal analysis (properties built before or after specific years)
- Visual mapping of tax-compliant vs non-compliant zones
- Feature engineering for supervised ML pipelines in Python (with scikit-learn)

---

## 👉 Next Steps

- Explore `scripts/` for PyQGIS integration scripts.

---

