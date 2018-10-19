import lxml.etree as et
import xlrd
import glob

with open("C:/Users/tp497dk/Desktop/pythonLearning/cinemaPython/newmissedcitylist2.txt", 'r') as f:
	x = f.readlines()

countrycodefile = xlrd.open_workbook("C:/Users/tp497dk/Downloads/country-code-name.xls")
sheet = countrycodefile.sheet_by_index(0)

countrycode = [x.strip().lower() for x in sheet.col_values(0)]
countryname = [x.strip().lower().title() for x in sheet.col_values(1)]
del countrycode[0]
del countryname[0]

countrycodedic={} #country code dictionary
for cn, cc in zip (countryname, countrycode):
	if cn not in countrycodedic:
		countrycodedic[cn] = cc 
#print(countrycodedic["United States"])



statecodefile = xlrd.open_workbook("C:/Users/tp497dk/Downloads/state-code-name.xls")
sheet = statecodefile.sheet_by_index(0)

statecode = [x.strip().lower() for x in sheet.col_values(1)]
statename = [x.strip().lower().title() for x in sheet.col_values(2)]
del statecode[0]
del statename[0]

statecodedic={} #country code dictionary
for sn, sc in zip (statename, statecode):
	if sn not in statecodedic:
		statecodedic[sn] = sc 
		
#print(statecodedic)



countrydic={}
dictionarydic={}


for i in x:	
		country=i.split(",")[-1].strip()
		
		if country not in countrydic:
			if country in ["United States", "Canada"]:
				countrydic[country] = {}
			else:
				countrydic[country] = []
		
		if country in ["United States", "Canada"]:
			statename = i.split(",")[-2].strip()
			if statename not in countrydic[country]:
				countrydic[country][statename] = []
			
			countrydic[country][statename].append(i.strip())
		else:
			countrydic[country].append(i.strip())

#for k, v in countrydic.items():
#	print(k,v)

notfound=[]	
def printkeywords(dic):
	if isinstance(dic, dict):
		for k, v in dic.items():
			print("<Keyword>")
			print("	<value>"+k+"</value>")
			print("	<description>"+k+"</description>")
			print("	<key>"+k.lower().replace(" ", "-")+"</key>")
			print("	<isAbstract>"+"Yes"+"</isAbstract>")
			printkeywords(v)
			print("</Keyword>")
			
	elif isinstance(dic, list):
		for a in dic:
			printkeywords(a)
			
			#printkeywords(a)	
	else:
		des=dic.split(",")[-2].strip()
		print("	<Keyword>")
		print("		<value>"+dic+"</value>")
		print("		<description>"+des+"</description>")
		print("		<key>"+des.lower().replace(" ", "-")+"-"+countrycodedic[dic.split(",")[-1].strip()]+"</key>")
		print("		<isAbstract>"+"No"+"</isAbstract>")
		print("		<Metadata>"+"folder:id"+"</Metadata>")
		print("	</Keyword>")
	
	
		
printkeywords(countrydic)



"""
count=0
for i in x:
	country = i.split(",")[-1].strip()
	
	root=et.Element("Keyword")
	Value=et.SubElement(root,"value")
	Value.text=country
	description=et.SubElement(root,"description")
	description.text=country
	key=et.SubElement(root,"key")
	key.text=country.lower()
	isAbstract=et.SubElement(root,"isAbstract")
	isAbstract.text="Yes"
	#tree=et.ElementTree(root)
	
	#we need a loop here 
	for x in countrydic[country]:
		rootcity=et.SubElement(root,"Keyword")
		Valuecity=et.SubElement(rootcity,"value")
		Valuecity.text=x
		descriptioncity=et.SubElement(rootcity,"description")
		descriptioncity.text=country
		keycity=et.SubElement(rootcity,"key")
		keycity.text=country.lower()
		isAbstractcity=et.SubElement(rootcity,"isAbstract")
		isAbstractcity.text="No"
	count=count +1
tree=et.ElementTree(root)
	
	
tree.write("C:/Users/tp497dk/Downloads/workEY/keywords.xml")
	
print (count)	
"""