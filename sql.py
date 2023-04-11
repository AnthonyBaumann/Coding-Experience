#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting workspace to the file path I Provided
arcpy.env.workspace= r"G:\325\acbaum1\Week 7\Lab6_ArcPy_DA_Cursors\Py_Ex08\data"
#this line sets the variable fc equal to the airports shapefile
fc = 'airports.shp'
#this line sets the variable sql_exp to an sql expression that takes all the/
#values of 'TOT_ENP' greater than 100,000.
sql_exp = '"TOT_ENP"> 100000'
#this line then creates a search cursor to loop through all the values of the /
#airports shapefile to find and print the names of airports the have values /
# of 'TOT_ENP' greater that 100,000.
cursor = arcpy.da.SearchCursor(fc, ["NAME"], sql_exp)                            
for row in cursor :
    print(row[0])
