#This line imports the acrpy tool to use further in the script
import arcpy
#this line sets the workspace to the file path that I provided to be worked out/
#of.
arcpy.env.workspace =r"G:\325\acbaum1\Week 5\Exercise03"
#this line clips together the lakes and basin feature to create the lake_myClip/
#feature in arcpro.
arcpy.Clip_analysis("lakes", "basin", "lakes_myClip")
