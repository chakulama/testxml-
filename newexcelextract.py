import lxml.etree as et
import xlrd
import glob

excelfile = xlrd.open_workbook("C:/Users/tp497dk/Downloads/POI_CityGuide_Fixes_final_16_10_ELT.xlsx")
sheet = excelfile.sheet_by_index(0)
resolved = [x for x in sheet.col_values(31)]##set= to elminate duplicates
cityfound = [x for x in sheet.col_values(32)]##set= to elminate duplicates

cities = []
for x, y  in zip(cityfound, resolved):
	if isinstance(x, int):
		cities.append(y)

cities = list(set(cities))

counter = 0
for city in cities:
	try:
		print(city)
	except:
		counter += 1

#print(counter)