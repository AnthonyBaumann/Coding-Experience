#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 6\Lab6_ArcPy_DA_Cursors\Py_Ex08\data"
#this line sets the variable fc equal to the airports shapefile
fc = "airports.shp"
#This line generates a unique name for a new shapefile that will /
#be created by the buffer analysis tool.
unique_name = arcpy.CreateUniqueName("buffer.shp")
#This creates a 5000 meter buffer around the features in the airports /
#shapefile and saves the result to the "unique_name" buffer shapefile. 
arcpy.Buffer_analysis(fc, unique_name, "5000 METERS")
