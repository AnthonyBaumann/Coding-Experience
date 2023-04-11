#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting the workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 11\Lab8_Raster_Objects\data"
#This line is assigning the name rasterlist to the a command that will list/
#the raster in he assigned workspace.
rasterlist = arcpy.ListRasters()
#This line iterates through all the rasters that the previous comand found/
#and prints them out
for raster in rasterlist:
 print(raster)
