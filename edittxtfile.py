import lxml.etree as et
import xlrd
import glob

folders = glob.glob("C:/Users/tp497dk/Downloads/workEY/HBD/HBD/**/*NearByhotels.txt", recursive=True)

filenameoutput = "C:/Users/tp497dk/Downloads/workEY/HBD/HBD/FullList.txt"
newfile=open(filenameoutput, 'w')
for folder in folders:
	foldername = "/".join(folder.split('\\')[:-1]);
	filenametoread = folder
	
	
	with open(filenametoread, 'r') as f:
		x = f.readlines()
	
	
	newfile.write("START" + '\n')
	newfile.writelines(x)
	newfile.write( "END" +'\n' )
	

print("done")	