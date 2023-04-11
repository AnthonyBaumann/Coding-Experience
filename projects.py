#This line is importing the arcpy tool to be used further in the code
import arcpy
#this line is setting the aprx variable to the "Austin.aprx" file which is in /
#the same workspace that this scri is saved in 
aprx = arcpy.mp.ArcGISProject("Austin.aprx")
#This line saves a copy of the designated aprx into the same mentioned folder/
#and is named "Austin_Copy
aprx.saveACopy("Austin_Copy.aprx")
#this line then deletes the reference to the project file in the script to /
#avoid a lock on the file
del aprx
