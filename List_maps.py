#This line is importing the arcpy tool to be used further in the code
import arcpy
#this line is setting the aprx variable to the "Austin.aprx" file which is in /
#the same workspace that this script is saved in 
aprx = arcpy.mp.ArcGISProject("Austin.aprx")
#this line sets the variable m to reference to the 'Region' map in the /
#original 'Austin' aprx 
m = aprx.listMaps("Region")[0]
#this line then changes the name of the varable m which wass originally 'Region'/
#to 'County'
m.name = "County"
#This line saves a copy of the designated aprx into the same mentioned folder/
#and is named "Austin_Copy" and contains the new named map
aprx.saveACopy("Austin_County.aprx")
#this line then deletes the reference to the project file in the script to /
#avoid a lock on the file
del aprx
