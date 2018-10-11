import lxml.etree as et
import xlrd
import glob



anythigdic= {
			"PKPART":"Art'otel",
			"CHIBSE":"Country Inn & Suites",
			"PIIBSE":"Park inn",
			"PKPBSE":"Park Plaza",	
			"RADBLU":"Radisson Blu",
			"RADCOL":"Radisson Collection",
			"RADRED":"Radisson Red",
			"RADGRN":"Radisson"
			}

name=[]
city=[]
country=[]
state=[]
service=[]

folders = glob.glob("C:/Users/tp497dk/Downloads/workEY/HBD/HBD/CIS/*")[:1]

for folder in folders:
	foldername = "/".join(folder.split('\\'));
	filenametoread = foldername + "/Hotel.xml"
	print ("fileneme to read:"+filenametoread)

	
	filenametowrite = foldername + "/Hotel2.xml"
	tree =et.parse(filenametoread)
	root=tree.getroot()
	
	
	#finding the hotel sita code from xml and replacing with fullname using anythigdic dictionary
	for element in root.iter("brand"):#iter is used to find its child name hotel
		#print("%s - %s" % (element.tag, element.text))
		element.text=anythigdic[element.text]

	#scraping data from metadata and printing it
	for element in root.iter("service"):
		service.append(element.text)
		
	for element in root.iter("name"):
		name.append(element.text)

	for element in root.iter("city"):
		city.append(element.text)
		
	for element in root.iter("country"):
		country.append(element.text)
		
	for element in root.iter("state"):
		state.append(element.text)
		

	tree.write(filenametowrite)

for x in list(set(service)): 
	print(x)
print ("-------------------")
for x in list(set(name)): 
	print(x)
print ("-------------------")
for x in list(set(city)): 
	print(x)
print ("-------------------")	
for x in list(set(country)): 
	print(x)
print ("-------------------")
for x in list(set(state)): 
	print(x)




print("done")



