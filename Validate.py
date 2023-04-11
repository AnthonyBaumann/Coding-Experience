#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting workspace to the file path I Provided
arcpy.env.workspace = "C:/PythonPro/Ex08"
#this line sets the variable fc equal to the airports shapefile
fc = "airports.shp"
#this line sets the variable newfield equal to the string "NEW CODE"
newfield = "NEW CODE"
#this line sets the variable fieldtype equal to the string "TEXT"
fieldtype = "TEXT"
#this line validates the name of the new field to ensure it is valid/
#in the shapefile and assigns it to the fieldname variable.
fieldname = arcpy.ValidateFieldName(newfield)
#These lines create a list of all the fields in the shapefile and create a list/
#of the names.
fieldlist = arcpy.ListFields(fc)
fieldnames = []
#These loops check the new field name is not already in the list and if /
#it is not the AddField_management function is used to add the new field /
#to the shapefile. If the new field already exists in the shapefile, a message /
#is printed indicating that no new field was added.
for field in fieldlist:
    fieldnames.append(field.name)
if fieldname not in fieldnames:
    arcpy.AddField_management(fc, fieldname, fieldtype, "", "", 12)
    print("New field has been added.")
else:
        print("Field name already exists, no new field was added.")
