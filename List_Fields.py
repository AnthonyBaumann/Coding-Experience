#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line allows any existing outputs to be overwritten.
arcpy.env.overwriteOutput = True
#This line is setting workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 6\Lab6_ArcPy_DA_Cursors\Py_Ex08\data"
#This line creates a list of all fields in the feature class 'cities.shp'.
fieldlist=arcpy.ListFields('cities.shp')
#this loop takes each field in the fieldlist and prints out the name of the /
#field and the data type of the field.
for field in fieldlist:
    print(field.name + ' ' + field.type)
