#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting the workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 10\data"
#this line is setting fc equal to the rivers shapefile within the data folder 
fc = "rivers.shp"
#this line is creating the search cursor which will be used to search, update, /
# and find data within the data folder with the feature class SHAPE@LENGTH after/
# the tool is ran.
with arcpy.da.SearchCursor(fc, ["SHAPE@LENGTH"]) as cursor:
 length = 0
#this for loop is iterating through the rows that the serach cursor provided and/
#is reformatting the output. 
 for row in cursor:
     length = length + row[0]
#this line is using the Describe function to be able to read the information of /
#the feature class
desc = arcpy.da.Describe(fc)
#this line is reformatting the data to show the unit at the end of the printed /
#statement based on the information from the describe function.
units = desc["spatialReference"].linearUnitName
#this line is printing the length to only two decimals and is also printing the/
#unit.
print(f"{length:.2f} {units}")
