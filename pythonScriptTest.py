import lxml.etree as et
tree =et.parse('Poi.xml')
root=tree.getroot()
	
landingLink=root[0][4].text

del root[0][4]

landinglink = et.SubElement(root[0], "landingLink")
General = et.SubElement(landinglink, "General")
Text= et.SubElement(General,"text")
Title= et.SubElement(General,"title")
ExternalUrl= et.SubElement(General,"ExternalUrl")
ExternalUrl.text=landingLink
Seo= et.SubElement(General,"seo")
Blank= et.SubElement(General,"blank")
iconClass= et.SubElement(General,"iconClass")
Pdf= et.SubElement(General,"pdf")
Rel= et.SubElement(General,"rel")


print(et.tostring(root))
tree.write("testresult.xml")


