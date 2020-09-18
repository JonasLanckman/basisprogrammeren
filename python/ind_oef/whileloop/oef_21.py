


teller = 1
tellerElkeTiende = 10
afdruk = ""


getal = int(input("Geef het eindgetal in: "))

while(teller <= getal):
	if teller == tellerElkeTiende:
	afdruk += " ,"
	tellerElkeTiende += 10
	elif (teller % 3 == 0):
		afdruk += str(teller) + "," + str(teller) + ","
	else:
		afdruk += str(teller) + ","
	teller += 1
print(afdruk[:-1])