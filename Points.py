#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting the workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 10\data"
#this line is setting fc equal to the dams shapefile within the data folder 
fc = "dams.shp"
#this line is creating the search cursor which will be used to search, update, /
# and find data within the data folder with the feature class SHAPE@XY after/
# the tool is ran and will return XY coords.
with arcpy.da.SearchCursor(fc, ["SHAPE@XY"]) as cursor:
 for row in cursor:
     x, y = row[0]
#this line is printing the XY coords with only 3 decimals 
     print("{0:.3f}, {1:.3f}".format(x, y))
