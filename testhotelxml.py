


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


for folder in folders:
	foldername = "/".join(folder.split('\\'));
	filenametoread = foldername + "/Hotel.xml"
	print ("filename to read:"+filenametoread)

	
	filenametowrite = foldername + "/Hotel2.xml"
	tree =et.parse(filenametoread)
	root=tree.getroot()
	
	del root[0][0][0][1]#delete longdescription
	del root[0][0][0][3]#delete alert message
	del root[0][0][0][4]#delete titleoverview
	
	for l in root[1].findall('nearbyHotels'):
		root[1].remove(l)
			

	for l in root[1].findall('sitaCode'):
		root[1].remove(l)
	for l in root[1].findall('backCode'):
		root[1].remove(l)	
		
	title=root[0][0][0][3].text
	del root[0][0][0][3] 
	Title=et.Element("title")
	Title.text=title
	root[0][0][0].insert(0,Title)
	
	
	for l in root[1].findall('status'):
		st= l.text
		root[1].remove(l)
		
	Status=et.Element("status")
	Status.text=st
	root[1].insert(9,Status)
	
	
	for l in root[0].findall('mediaList'):
		root[0].remove(l)
		root[0].append(l)
		
	Status=et.Element("status")
	Status.text=st
	root[1].insert(9,Status)
	
	
	
	
	#del root[0][1]
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



