#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting the workspace to the file path I Provided
arcpy.env.workspace = r"G:\325\acbaum1\Week 11\PythonScripting_Ex10_Data\Ex10"
#This line sets the outraster to the tool that will create slope from the given/
#file
outraster = arcpy.sa.Slope("elevation")
#This saves the temporary slope file to a permanent location
outraster.save("slope")

