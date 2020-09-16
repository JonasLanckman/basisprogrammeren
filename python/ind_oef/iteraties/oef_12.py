


beginGetal = int(input("Geef het begin getal in: "))
eindGetal = int(input("Geef het eindgetal in: "))


for x in range(beginGetal , eindGetal , + 1):
	if x > 1: 
		for y in range(2,x):
			if (x % y) == 0:
				break
		else:
			print(x)	