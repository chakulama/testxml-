import lxml.etree as et
import xlrd
import glob

excelfile = xlrd.open_workbook("C:/Users/tp497dk/Downloads/edited_POI Missing Cities (1).xlsx")
sheet = excelfile.sheet_by_index(0)
cityexcel = [x.strip() for x in sheet.col_values(1)]##set= to elminate duplicates
cityexcel = (set(cityexcel))
print (len(cityexcel))




tree =et.parse("C:/Users/tp497dk/Downloads/keyCity.xsd")
root=tree.getroot()
l=[]
for x in root [0][0]:
	l.append(x.attrib["value"])

l= set(l)

result= cityexcel-l

result = list(result)
l = list(l)

for i in range(len(result)):
	word = result[i].split(',')[0]
	for j in range(len(l)):
		a=l[j]
		if word in a.split(','):
			print (f"{result[i]:<50}       {l[j]:<50}")
	


	


	
