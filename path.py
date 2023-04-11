path = "G:/325/acbaum1/Week 4"
#here I set a file path for this /code so that the next lines/
#can gather the required variables

pathlist = path.split("/")
#This line splits the path into strings seperated by each "/"

lastpath = pathlist[-1]
#This line identifies the last sting in the path which in Week 4

print(lastpath)
#This print statement is taking the variable lastpath and printing it out/
#in the shell. Essetially this script is setting a file path, then separating/
#each folder, and then taking the last folder in the path and printing it.
