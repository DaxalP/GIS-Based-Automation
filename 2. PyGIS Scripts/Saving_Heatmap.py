from qgis.core import QgsProject, QgsRasterFileWriter, QgsCoordinateReferenceSystem
from qgis.core import QgsMapSettings, QgsMapRendererParallelJob
from qgis.PyQt.QtGui import QImage, QPainter
from qgis.PyQt.QtCore import QSize

# Get the heatmap layer (replace with your actual layer name)
layer_name = "Unpaid Tax Heatmap"
heatmap_layer = QgsProject.instance().mapLayersByName(layer_name)[0]

# Set output path
output_path = "C:/Users/dpiso/OneDrive/Desktop/NIUA_Intern/GIS/unpaid_heatmap.tif"

# Prepare map settings
settings = QgsMapSettings()
settings.setLayers([heatmap_layer])
settings.setOutputSize(QSize(2000, 2000))  # Adjust resolution here
settings.setExtent(heatmap_layer.extent())
settings.setDestinationCrs(QgsCoordinateReferenceSystem("EPSG:4326"))

# Render map
image = QImage(settings.outputSize(), QImage.Format_ARGB32_Premultiplied)
image.fill(0)

painter = QPainter(image)
job = QgsMapRendererParallelJob(settings)
job.start()
job.waitForFinished()
job.renderedImage().save(output_path, "tif")
painter.end()

print(f"✅ Heatmap exported to: {output_path}")