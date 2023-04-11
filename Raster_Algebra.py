#These lins are importing the arcpy and arcpy.sa tool to be used further in/
#the code
import arcpy
from arcpy.sa import *
#This line is setting the workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 11\PythonScripting_Ex10_Data\Ex10"
#this line sets the variable elevraster to the provided elevation Rasters
elevraster = arcpy.Raster("elevation")
#This line sets the variable slope to the value created by the slope tool /
#derived from the elevraster variable
slope = Slope(elevraster)
#These lines set map algebra to indicate slope less than 20 degrees and /
#elevation less than 2500 meters and saves these slope values
goodslope = slope < 20
goodelev = elevraster < 2500
goodfinal = goodslope & goodelev
goodfinal.save("final")
