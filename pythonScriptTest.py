import lxml.etree as et
import xlrd
import glob


excelfile = xlrd.open_workbook("C:/Users/tp497dk/Downloads/workEY/New_Web_Property_Data.xlsx")
sheet = excelfile.sheet_by_index(0)
hotelname = [x.strip() for x in sheet.col_values(10)]
sitacode = [x.strip() for x in sheet.col_values(12)]
hotelname.pop(0)
sitacode.pop(0)
anythigdic=dict(zip(sitacode,hotelname))

type=[]
city=[]
country=[]
state=[]

folders = glob.glob("C:/Users/tp497dk/Downloads/workEY/POIs-05-10-2018/POIs/POI/*")[12:30]

for folder in folders:
	foldername = "/".join(folder.split('\\')) + "/POI/";
	filenametoread = foldername + "Poi.xml"
	print (filenametoread)

	
	filenametowrite = foldername + "Poi2.xml"
	tree =et.parse(filenametoread)
	root=tree.getroot()
		
	landingLink=root[0][4].text

	del root[0][4]

	landinglink = et.SubElement(root[0], "landingLink")
	attributes = landinglink.attrib
	attributes["schema"]="Link"
	General = et.SubElement(landinglink, "General")
	Text= et.SubElement(General,"text")
	Title= et.SubElement(General,"title")
	ExternalUrl= et.SubElement(General,"externalUrl")
	ExternalUrl.text=landingLink
	Seo= et.SubElement(General,"seo")
	Blank= et.SubElement(General,"blank")
	iconClass= et.SubElement(General,"iconClass")
	Pdf= et.SubElement(General,"pdf")
	Rel= et.SubElement(General,"rel")

	
	


	#finding the hotel sita code from xml and replacing with fullname using anythigdic dictionary
	for element in root.iter("hotel"):#iter is used to find its child name hotel
		#print("%s - %s" % (element.tag, element.text))
		if(element.text == None):
			pass
		else:
			element.text=anythigdic[element.text]

	#scraping data from metadata and printing it
	for element in root.iter("type"):
		type.append(element.text)

	for element in root.iter("city"):
		city.append(element.text)
		
	for element in root.iter("country"):
		country.append(element.text)
		
	for element in root.iter("state"):
		state.append(element.text)
		

	tree.write(filenametowrite)

for x in list(set(type)): 
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



