#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 7\Lab6_ArcPy_DA_Cursors\Py_Ex08\data"
#This line sets the variable fc to airports.shp
fc= "airports.shp"
#this line creates the sesarch cursor that will find each name in the 'airports'/
#shapefile.
cursor = arcpy.da.SearchCursor(fc,['NAME'])
# This loop then iterates through each row in the cursor and then prints the /
#name of each airport in the 'airport' shapefile.
for row in cursor:
    print('Airport name = {0}'.format(row[0]))
