#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting the workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 6\Lab6_ArcPy_DA_Cursors\Py_Ex08\data"
#this line is setting fc equal to the airports shapefile within the data folder 
fc = "airports.shp"
#this line creates an insert cursor that will insert a new entry into the airports/
#data frame
with arcpy.da.InsertCursor(fc, "NAME") as cursor:
    cursor.insertRow(["New Airport"])
