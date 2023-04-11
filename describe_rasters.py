#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting the workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 11\Lab8_Raster_Objects\data"
#This line is assigning the name raster to the raster tm.img from the assigned/
#workspace.
raster = "tm.img"
#This line uses the describe tool to get the information about the raster I /
#assigned previously
desc = arcpy.da.Describe(raster)
#These next lines iterate over the information derived from the raster and also/
#sets an x and y value as mean cell height and mean cell width repectively
for rband in desc["children"]:
    bandname = rband["baseName"]
    x = rband["meanCellHeight"]
    y = rband["meanCellWidth"]
#these next two lines then print a formated statement in the whatever unit the /
#spatial refernece is in to the 7th decimal place
    spatialref = desc["spatialReference"]
    units = spatialref.angularUnitName
    print("The resolution of {0} is {1:.7f} by {2:.7f} {3}.".format(bandname, x, y, units))















