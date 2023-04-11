#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 7\Lab6_ArcPy_DA_Cursors\Py_Ex08\data"
#this line sets the variable fc equal to the airports shapefile
fc = 'airports.shp'
# Define the field delimiter used for the SQL expression in this case it is the/
#airports feature STATE.
delimfield = arcpy.AddFieldDelimiters(fc, 'STATE')
#this line defines the SQL expression to select all the value /
#in the 'STATE' field that are not equal to 'AK'
sql_exp = delimfield + "<>'AK'"
#this line sets an update cursor in the airports shapefile and use the sql /
# expression to filter out all the names.
with arcpy.da.UpdateCursor(fc,['STATE'], sql_exp) as cursor:
# then this for loop iterates through all the names and assigns the row with/
#AK and updates the shapefile.
    for row in cursor:
        row[0] = 'AK'
        cursor.updateRow(row)
    
