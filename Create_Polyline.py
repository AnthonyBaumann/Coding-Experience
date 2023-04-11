#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is importing the fileinput tool to be used further in the code
import fileinput
#This line is importing the os tool to be used further in the code
import os
#This line is setting the workspace to the file path I Provided
ws = r"G:\325\acbaum1\Week 10\data"
#This line is setting the arcpy environment workspace to ws
arcpy.env.workspace = ws
#This line is allowing the workspace to be overwritten if needed
arcpy.env.overwriteOutput = True
#this line is creating a new featureclass that will store the newly created /
#ployline
newfc = "newpolyline.shp"
#this line is now setting the new polyline feature to the same spatial reference as the /
#dams shapefile
arcpy.CreateFeatureclass_management(ws, newfc,"Polyline", spatial_reference = "dams.shp")
#this line opens the coordinates text file to be used to create the vertices for the new /
#polyline
infile = os.path.join(ws, "coordinates.txt")
#This insert cursor is then used to create new rows and an array object to contain the new/
#point object
with arcpy.da.InsertCursor(newfc, ["SHAPE@"]) as cursor:
    array = arcpy.Array()
#this line then reads the text file, seperates the text into seperate strings,/
#and then iterates over the text file to create a point object for each line /
#in the text file.
    for line in fileinput.input(infile):
        ID, X, Y = line.split()
        array.add(arcpy.Point(X, Y))
    cursor.insertRow([arcpy.Polyline(array)])
    fileinput.close()
