#This line imports the acrpy tool to use further in the script
import arcpy
#this line is creating a workspace using the file path I provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 5\Lab5_PyWindow_Geoprocessing\Py_Ex05\data"
#This line overwrites any output this code produces to save the most current/
#iteration in arcPRO.
arcpy.env.overwriteOutput = True
#this line creates a new clipped feature using the bike_routes and parks shapefile/
#to then create a new clipped feature bike_clip
newclip = arcpy.Clip_analysis("bike_routes.shp", 
"parks.shp", "bike_clip.shp")
#this line gets feedback on if there is a feature called bike_clip and then if there is /
#the rest of the script provides a messege telling the user if the script ran successfuly.
fcount = arcpy.GetCount_management("bike_clip.shp")
msgCount = newclip.messageCount
print(newclip.getMessage(msgCount-1))
