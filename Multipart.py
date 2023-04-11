#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting the workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 10\data"
#this line is setting fc equal to the hawaii shapefile within the data folder 
fc = "hawaii.shp"
#this line is setting the cursor to the search cursor which will be used to find data within/
#the filepath folder with the feature classes OID@ and SHAPE@ to find all of the/
#vertices in the hawaii shapefile.
cursor = arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@"])
for row in cursor:
    print("Feature {0}: ".format(row[0]))
    partnum = 0
    for part in row[1]:
        print("Part {0}: ".format(partnum))
        for point in part:
            print("{0:.2f}, {1:.2f}".format(point.X, point.Y))
        partnum += 1
