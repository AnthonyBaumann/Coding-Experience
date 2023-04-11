#This line is importing the arcpy tool to be used further in the code
import arcpy
#this line is setting the aprx variable to the "Austin.aprx" file which is in /
#the same workspace that this script is saved in 
aprx = arcpy.mp.ArcGISProject("Austin.aprx")
#this line sets the variable m to reference to the 'Downtown' map in the /
#original 'Austin' aprx
m = aprx.listMaps("Downtown")[0]
#this line sets the variable lyrs to the parks layer from the variable m which/
#contains the 'Downtown' map
lyr = m.listLayers("parks")[0]
#this line then sets the variable sym to the layer symbology of the lyr variable
sym = lyr.symbology
#this line then sets the variable red to the rgb code for red 
red = {"RGB": [100, 175, 0, 100]}
#these next lines then checks to make sure the parks layer is the right type of/
#layer and will support the render of the color.
if lyr.isFeatureLayer and hasattr(sym, "renderer"):
    sym.renderer.symbol.color = red
    lyr.symbology = sym
#these lines then save a copy of the project as the given name and then deletes
#the reference to the project file in the script to avoid a lock on the file
aprx.saveACopy("Austin_Symbology.aprx")
del aprx
