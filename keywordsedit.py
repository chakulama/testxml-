import lxml.etree as et
import xlrd
import glob

with open("C:/Users/tp497dk/Desktop/pythonLearning/cinemaPython/newmissedcitylist.txt", 'r') as f:
	x = f.readlines()

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
#	print(v)

	
def printkeywords(dic):
	if isinstance(dic, dict):
		for k, v in dic.items():
			print("<Keyword>")
			print("	<value>"+k+"</value>")
			print("	<description>"+k+"</description>")
			print("	<key>"+k.lower()+"</key>")
			print("	<isAbstract>"+"Yes"+"</isAbstract>")
			printkeywords(v)
			print("</Keyword>")
	elif isinstance(dic, list):
		for a in dic:
			printkeywords(a)
	else:
		des=dic.split(",")[-2].strip()
		print("	<Keyword>")
		print("		<value>"+dic+"</value>")
		print("		<description>"+des+"</description>")
		print("		<key>"+des.lower()+"</key>")
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