from qgis.core import (
    QgsVectorLayer, QgsProject, QgsFeatureRequest,
    QgsVectorFileWriter, QgsCoordinateTransformContext
)
import os

# Load the full CSV layer (do not add to map)
csv_path = "C:/Users/dpiso/OneDrive/Desktop/NIUA_Intern/GIS/tax_compliance.csv"
uri = f"file:///{csv_path}?delimiter=,&xField=Longitude&yField=Latitude&crs=EPSG:4326"
full_layer = QgsVectorLayer(uri, "TempLayer", "delimitedtext")

if not full_layer.isValid():
    print("❌ Failed to load the CSV.")
else:
    # Filter to only unpaid entries
    expr = "\"Tax_Compliance\" = 'False'"
    filtered_layer = full_layer.materialize(QgsFeatureRequest().setFilterExpression(expr))

    # Save as GeoPackage (recommended)
    save_path = "C:/Users/dpiso/OneDrive/Desktop/NIUA_Intern/GIS/unpaid_properties.gpkg"
    layer_name = "Unpaid_Tax"

    options = QgsVectorFileWriter.SaveVectorOptions()
    options.driverName = "GPKG"
    options.layerName = layer_name

    result, error = QgsVectorFileWriter.writeAsVectorFormatV2(
        filtered_layer,
        save_path,
        QgsProject.instance().transformContext(),
        options
    )

    if result == QgsVectorFileWriter.NoError:
        print("💾 GeoPackage saved.")

        # Load from GeoPackage
        loaded_layer = QgsVectorLayer(f"{save_path}|layername={layer_name}", "Unpaid Property Tax", "ogr")
        if loaded_layer.isValid():
            QgsProject.instance().addMapLayer(loaded_layer)
            print("✅ Layer added from GeoPackage.")
        else:
            print("❌ Could not load from GeoPackage.")
    else:
        print("❌ Failed to save filtered layer:", error)
