from qgis.core import (
    QgsVectorLayer, QgsProject, QgsHeatmapRenderer,
    QgsGradientColorRamp, QgsSymbol
)
from qgis.PyQt.QtGui import QColor

# Load the saved GPKG layer
gpkg_path = "C:/Users/dpiso/OneDrive/Desktop/NIUA_Intern/GIS/unpaid_properties.gpkg"
layer_name = "Unpaid_Tax"
heat_layer = QgsVectorLayer(f"{gpkg_path}|layername={layer_name}", "Unpaid Tax Heatmap", "ogr")

if not heat_layer.isValid():
    print("❌ Failed to load layer.")
else:
    # Color ramp: transparent (0 alpha) → red
    color_ramp = QgsGradientColorRamp(
        QColor(255, 0, 0, 0),   # transparent red (low density)
        QColor(255, 0, 0, 255)  # solid red (high density)
    )

    renderer = QgsHeatmapRenderer()
    renderer.setColorRamp(color_ramp)
    renderer.setRadius(20)  # Tune this to tighten or soften effect
    renderer.setWeightExpression("")  # All points equal weight

    # Apply heatmap renderer
    heat_layer.setRenderer(renderer)
    QgsProject.instance().addMapLayer(heat_layer)

    print("🔥 Heatmap with transparent background added.")
