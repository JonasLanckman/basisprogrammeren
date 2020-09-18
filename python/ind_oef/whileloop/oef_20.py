



x = 1
getal = int(input("Geef getal in: "))
afdrukOpScherm = ""

while (x <= getal):
	getal = getal * x
	afdrukOpScherm = afdrukOpScherm + str(x) + "x"
	x += 1
print(afdrukOpScherm + str(x+1) + "=" + str(getal))