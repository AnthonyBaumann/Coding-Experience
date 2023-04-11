#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting the workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 10\data"
#this line is setting fc equal to the rivers shapefile within the data folder 
fc = "rivers.shp"
#this line is creating the search cursor which will be used to find data within/
#the filepath folder with the feature classes OID@ and SHAPE@ to find all of the/
#vertices in the rivers shapefile.
with arcpy.da.SearchCursor(fc, (["OID@", "SHAPE@"])) as cursor:
 for row in cursor:
#these print statements are printing the feature number and then printing the/
#the vertices from that specific feature.
     print("Feature {0}: ".format(row[0]))
     for point in row[1].getPart(0):
         print("{0:.3f}, {1:.3f}".format(point.X, 
point.Y))
