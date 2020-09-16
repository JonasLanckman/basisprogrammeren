

getal = int(input("Geef getal op: "))
afdrukOpScherm = ""
for x in range(1, getal):
	getal = getal * x
	afdrukOpScherm = afdrukOpScherm + str(x) + "x"
print(afdrukOpScherm + str(x+1) + "=" + str(getal))