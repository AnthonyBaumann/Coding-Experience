import arcpy
#this line imports the arcpy tool to be used further in the script
arcpy.env.workspace = r"G:\325\acbaum1\Week 4\Py_Ex07\data"
#this line is creating a workspace using the file path I provided
fclist = arcpy.ListFeatureClasses()
#this line creates a list of all the features from the provided workspace.
for fc in fclist:
#this line specifies each individual feature in the previously created feature/
#list
    desc = arcpy.da.Describe(fc)
#This line sets desc to the tool in arcpy that allows for the description of /
#each feature
    print(f'{desc["baseName"]}: {desc["shapeType"]}')
#this print statement prints the description of the feature from the feature /
#class list and the corresponding shape type
    
