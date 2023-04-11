#This line imports the acrpy tool to use further in the script
import arcpy
#this line sets the workspace to the file path that I provided to be worked out/
#of.
arcpy.env.workspace =r"G:\325\acbaum1\Week 5\Lab5_PyWindow_Geoprocessing\Py_Ex05\data"
#this line sets the input shapefile to the parks shape file in arcPro.
in_fc = "parks.shp"
#this line sets the output shapefile to be creted as the parks_centroid shape file in arcPro.
out_fc = "parks_centroid.shp"
#this loop sets the arcPro tool featureToPoint Managment to use the given inputs and outputs/
# to run the tool within arcPro.
if arcpy.ProductInfo() == "ArcInfo":
 arcpy.FeatureToPoint_management(in_fc, out_fc)
else:
 print("An ArcInfo license is not available.")
