from qgis.core import (
    QgsProject,
    QgsVectorLayer,
    QgsCategorizedSymbolRenderer,
    QgsRendererCategory,
    QgsSymbol
)
from PyQt5.QtGui import QColor

# Get your loaded layer
layer = QgsProject.instance().mapLayersByName("Property Points")[0]

# Define categories (label, color)
property_types = {
    'Residential': 'blue',
    'Commercial': 'red',
    'Mixed': 'purple',
    'Vacant': 'gray',
    'Industrial': 'orange'
}

categories = []

# Create symbol for each property type
for p_type, color in property_types.items():
    symbol = QgsSymbol.defaultSymbol(layer.geometryType())
    symbol.setColor(QColor(color))
    category = QgsRendererCategory(p_type, symbol, p_type)
    categories.append(category)

# Apply categorized renderer on 'Property_Type'
renderer = QgsCategorizedSymbolRenderer('Property_Type', categories)
layer.setRenderer(renderer)
layer.triggerRepaint()

print("✅ Layer styled by Property_Type.")
