
teller = 0
getal = 0
getallenReeks = []

while(getal >= 0):
	getallenReeks.append(int(input("Geef getal {} in: ".format(teller+1))))
	getal = getallenReeks[teller]
	teller += 1
hoeveelsteGetal = int(input("Het hoeveelste getal wil je zien? "))
hoeveelsteGetal = getallenReeks[hoeveelsteGetal-1]
print(hoeveelsteGetal)












