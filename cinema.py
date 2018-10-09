films={
"Star is Born": [18,10],
"Ant Men 2": [10,10],
"a":[18,10]
}

while True:
	choice=input("what film would like to watch?:").strip()
	
	filmss = [x.lower() for x in films.keys()]
	if choice.lower() in filmss:
		print("aaaaa: ")
	else:
		print("We dont have that film: ")