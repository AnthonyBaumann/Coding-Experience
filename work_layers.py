#This line is importing the arcpy tool to be used further in the code
import arcpy
#this line is setting the aprx variable to the "Austin.aprx" file which is in /
#the same workspace that this script is saved in 
aprx = arcpy.mp.ArcGISProject("Austin.aprx")
#this line sets the variable m to reference to the 'Downtown' map in the /
#original 'Austin' aprx
m = aprx.listMaps("Downtown")[0]
#this line sets the variable lyrs to reference to the map layers from the /
#variable m which contains the 'Downtown' map
lyrs = m.listLayers()
#these next few lines then iterate throught all the layers in the map and /
#prints each layer based on if the layer is a basemap layer or a feature layer/
#and thendeletes the reference to the project file in the script to avoid a lock/
#on the file
for lyr in lyrs:
    if lyr.isBasemapLayer:
        print(lyr.name + " is a basemap layer")
    if lyr.isFeatureLayer:
        print(lyr.name + " is a feature layer")
del aprx
