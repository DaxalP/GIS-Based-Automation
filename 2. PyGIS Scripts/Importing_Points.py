from qgis.core import QgsVectorLayer, QgsProject

csv_path = "C:/Users/dpiso/OneDrive/Desktop/NIUA_Intern/GIS/cleaned_clusters.csv"
layer_name = "Property Points"

# Simplified URI — remove escape/quote 
uri = f'file:///{csv_path}?delimiter=,&xField=Longitude&yField=Latitude&crs=EPSG:4326'
print("Using URI:", uri)

layer = QgsVectorLayer(uri, layer_name, 'delimitedtext')

if layer.isValid():
    QgsProject.instance().addMapLayer(layer)
    print(f"✅ Layer '{layer_name}' added successfully!")
else:
    print("❌ Failed to load the CSV layer.")
