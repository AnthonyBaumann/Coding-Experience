#This line is importing the arcpy tool to be used further in the code
import arcpy
#This line is setting workspace to the file path I Provided
arcpy.env,workspace = r"G:\325\acbaum1\Week 7\Lab6_ArcPy_DA_Cursors\Py_Ex08\data"
#this line sets the variable infc to the airports shapefile that will then be/
#used as the input shapefile for the selection.
infc = 'airports.shp'
#this line sets the variable outfc to the airports_anchorage shapefile that/
#will then be used as the output file name that will be created.
outfc = 'airports_anchorage.shp'
#This line creates a variable 'delim_field' that contains the input "County"/
#so it can be used in SQL.
delim_field = arcpy.AddFieldDelimiters(infc, "County")
#This line creates the variable 'sql_exp' that contains the delim_field/
#so that this expression will only select features in the input shapefile/
#that have the "County" field named "Anchorage Borough"./
sql_exp = delim_field + " = Anchorage Borough' "
#This line uses the arcpy.Select_analysis function to create a new shapefile/
#called 'airports_anchorage.shp' that will only have the data from the sql/
#expression.
arcpy.Select_analysis (infc, outfc, sql_exp)



#*** ChatGPT Guidence***
