#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting the workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 6\Lab6_ArcPy_DA_Cursors\Py_Ex08\data"
#this line is setting fc equal to the airports shapefile within the data folder 
fc = "airports.shp"
#this line is creating the update cursor which will be used to change and update/
#data within the data folder after a tool is ran.
with arcpy.da.UpdateCursor(fc, ["TOT_ENP"]) as cursor:
#this for loop is now searching each of the values in TOT_ENP to find values under /
#100,000 and deleting them
    for row in cursor:
        if row[0] < 100000:
            cursor.deleteRow()
