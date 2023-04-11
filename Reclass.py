#These lins are importing the arcpy and arcpy.sa tool to be used further in/
#the code
import arcpy
from arcpy.sa import *
#This line is setting the workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 11\PythonScripting_Ex10_Data\Ex10"
#This line sets the variable myremap to the given parameters
myremap = RemapValue([[41,1], [42,2], [43,3]])
#These lines set the variable outreclass to the reclassification of the landcover /
#tif file and with the set parameters
outreclass = Reclassify("landcover.tif", "VALUE", myremap,"NODATA")
outreclass.save("lc_recl")
