#this line imports the arcpy tool and the os toolto be used further in the script
import arcpy
import os
#this line is creating a workspace using the file path I provided
arcpy.env.workspace = "G:/325/acbaum1/Week 4/Py_Ex07/data"
#This line overwrites any output this code produces to save the most current/
#iteration in arcPRO.
arcpy.env.overwriteOutput = True
#This line sets the geodatabase to be created  
fgdb = "Demo.gdb"
#this line creates a feature list and adds each feature from the list into a /
#predefined geodatabase
try:
    fclist = arcpy.ListFeatureClasses()
    for fc in fclist:
        desc = arcpy.da.Describe(fc)
        outfc = os.path.join(fgdb, desc["baseName"])
        arcpy.CopyFeatures_management(fc, outfc)
except arcpy.ExecuteError:
    print(arcpy.GetMessages(2))
except:
    print("There has neen a nontool error.")
