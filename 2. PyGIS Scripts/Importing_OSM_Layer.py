from qgis.core import QgsRasterLayer, QgsProject

# OSM Standard XYZ tile URL
osm_url = "type=xyz&url=https://tile.openstreetmap.org/{z}/{x}/{y}.png"

# Create raster layer
osm_layer = QgsRasterLayer(osm_url, "OSM Standard", "wms")

# Add to QGIS if valid
if osm_layer.isValid():
    QgsProject.instance().addMapLayer(osm_layer)
    print("✅ OSM Standard basemap added successfully!")
else:
    print("❌ Failed to add OSM Standard basemap.")
