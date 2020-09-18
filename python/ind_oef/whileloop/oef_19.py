


teller = 1
aantalSterren = 11
afdruk=""

letter = input("Geef een letter: ")
while(teller <= aantalSterren):
	afdruk = afdruk + letter
	teller += 1
print(afdruk)
teller = 1
while(teller <= aantalSterren):
	print("     " + letter)
	teller += 1