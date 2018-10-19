import lxml.etree as et
import xlrd
import glob


folders = glob.glob("C:/Users/tp497dk/Downloads/workEY/HBD/HBD/**/*Hotel.xml", recursive=True)
excelfile = xlrd.open_workbook("C:/Users/tp497dk/Downloads/New_Web_Property_Data.xlsx")
sheet1 = excelfile.sheet_by_index(0)
sitacode = [x.strip() for x in sheet1.col_values(12)]
hotelname = [x.strip() for x in sheet1.col_values(10)]

dic={}
notfound=[]

for sitac, hn in zip (sitacode, hotelname):
	if sitac not in dic:
		dic[sitac] = hn 
		


for folder in folders:
	foldername = "/".join(folder.split('\\')[:-1]);
	filenametoread = folder
	filenameoutput = foldername + "/NearByhotels.txt"
	tree =et.parse(filenametoread)
	root=tree.getroot()
	
	nearbyhotelslist=[]
	
	for nearbyhotels in root.iter("nearbyHotels"):
		if nearbyhotels.text and nearbyhotels.text != "":
			nearbyhotelslist.append(nearbyhotels.text)
		
	
	
	hotelname=[x.text for x in root.iter("name")][0]
	if nearbyhotelslist:
		
		f=open(filenameoutput, 'w')
		f.write(hotelname+ '\n')
		for l in nearbyhotelslist:
			if l:
				try:
					f.write(l+ "    %     " +dic[l]+ '\n')
				except:
					notfound.append(l)					

a=open("C:/Users/tp497dk/Downloads/workEY/HBD/HBD/notfound.txt", 'w')					
for l in notfound:
	a.write(l+'\n')

print("Not found output is written in C:/Users/tp497dk/Downloads/workEY/HBD/HBD/notfound.txt ")	
print("done")				