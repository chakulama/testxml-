import xlrd

book3 = xlrd.open_workbook("book3.xlsx")
poi = xlrd.open_workbook("POI_CityGuide_global_final_07_10.xlsx")

sheetBook3 = book3.sheet_by_index(0)
sheetPoi = poi.sheet_by_index(0)

poicountry = [x.strip().lower() for x in sheetPoi.col_values(16)]##set= to elminate duplicates
poicity = [x.strip().lower() for x in sheetPoi.col_values(17)]
poidic={}

for city, country in zip (poicity, poicountry):
	if city not in poidic:
		poidic[city] = country 

poicountry = [x.lower() for x in poicountry]##x.lower to lower down alphabets

l = [x.strip() for x in sheetPoi.col_values(17)]




c=[]

for x, city in enumerate(l):
	try:
		print (x, city)
		c.append(city)
		
	except:
		pass
		#print(x)
		
poicity = list(set(c)) 
poicity = [x.lower() for x in poicity]


	
	
Bookcity =list(set( sheetBook3.col_values(2)))
Bookcity = [x.lower() for x in Bookcity]

difference=(list(set(poicity) - set(Bookcity)))

print ("differences ------------")
for x in difference:
	print(poidic[x] + "--" + x)

print (len(difference))	


