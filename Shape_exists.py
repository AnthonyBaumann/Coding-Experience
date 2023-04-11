#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting workspace to the file path I Provided
arcpy.env.workspace= r"G:\325\acbaum1\Week 7\Lab6_ArcPy_DA_Cursors\Py_Ex06\data"
#this line sets the variable fc equal to the cities shapefile
fc='cities.shp'
#this line sets the variable newfc equal to the cities_copy shapefile
newfc='cities_copy.shp'
#this if statement then checks to see if there is already a feature called /
#cities and if there is it created a new feature called cities_copy.
if arcpy.Exists(fc):
    arcpy.CopyFeatures_management(fc,newfc)

