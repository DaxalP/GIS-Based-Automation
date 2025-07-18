from qgis.core import QgsProject, QgsVectorFileWriter
import os

# 🔧 Set your output directory
output_dir = "C:/Users/dpiso/OneDrive/Desktop/NIUA_Intern/GIS/Cloud_Uploading_Files"
os.makedirs(output_dir, exist_ok=True)

# 🔁 Export each vector layer
for layer in QgsProject.instance().mapLayers().values():
    if layer.type() == layer.VectorLayer:
        name = layer.name().replace(" ", "_")
        output_path = os.path.join(output_dir, f"{name}.geojson")
        result, error = QgsVectorFileWriter.writeAsVectorFormatV2(
            layer,
            output_path,
            QgsProject.instance().transformContext(),
            QgsVectorFileWriter.SaveVectorOptions()
        )
        if result == QgsVectorFileWriter.NoError:
            print(f"✅ Exported: {output_path}")
        else:
            print(f"❌ Error exporting {layer.name()}: {error}")
