import lxml.etree as et
import xlrd
import glob

count=0
folders = glob.glob("C:/Users/tp497dk/Downloads/workEY/HBD/HBD/CIS/*")[:20]
for folder in folders:
	foldername = "/".join(folder.split('\\'));
	filenametoread = foldername + "/Hotel.xml"
	filenametowrite = foldername + "/TestLink.xml"
	tree =et.parse(filenametoread)
	root=tree.getroot()
	
	longdescription=root[0][0][0][1].text

	Textlink= et.Element("TextLink")
	General1= et.SubElement(Textlink,"General")
	text1=et.SubElement(General1,"text")
	attributes= text1.attrib
	attributes["schema"]="TextTitleDescription"
	General2= et.SubElement(text1,"General")	
	title=et.SubElement(General2,"title")
	description=et.SubElement(General2,"description")
	description.text=longdescription

	link = et.SubElement(General1,"link")
	attributes = link.attrib
	attributes["schema"]="Link"
	General3= et.SubElement(link,"General")

	tree=et.ElementTree(Textlink)

	tree.write(filenametowrite)
	count= count +1
print("No. of file created:",  count)
	
		
	





