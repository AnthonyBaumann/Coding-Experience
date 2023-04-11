#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting the workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 6\Lab6_ArcPy_DA_Cursors\Py_Ex08\data"
#This line creates a list of all feature classes in the current workspace
fclist = arcpy.ListFeatureClasses()
#this loop then iterates through the feature classes list and retrieves the /
#data type, name, and shape type of the features in the list and then prints /
#out the the gathered information.
for fc in fclist:
 fcdesc = arcpy.da.Describe(fc)
 dtype = fcdesc["dataType"]
 name = fcdesc["name"]
 stype = fcdesc["shapeType"]
 print(f"{dtype} {name} has shapetype {stype}")
