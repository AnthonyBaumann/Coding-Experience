#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is importing the os tool to be used further in the code
import os
#This line is setting ws to the file path I Provided
ws = r"G:\325\acbaum1\Week 6\Lab6_ArcPy_DA_Cursors\Py_Ex08\data"
#This line assigns the variable 'fgdb' to "copy.gdb",/
#which will be the name of the file geodatabase that will be created.
fgdb= 'copy.gdb'
#This line creates a new file geodatabase in the workspace
arcpy.CreateFileGDB_management(ws,fgdb)
#this line sets the arcpy workspace to the variable ws which is I assigned /
#a file path to earlier.
arcpy.env.workspace=ws
#This line creates a list of feature classes in the workspace
fclist=arcpy.ListFeatureClasses()
#this loop then iterates through the feature classes list and retrieves the /
#names of the features in the list and then creates a new feature class path /
#using the workspace, the geodatabase, and the current feature name.
for fc in fclist:
    fcname = arcpy.da.Describe(fc)["baseName"]
    newfc = os.path.join(ws, fgdb, fcname)
    arcpy.CopyFeatures_management(fc, newfc)
