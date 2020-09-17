som = 0

getalA = 1



while (getalA <= 5):
	print("Geef getal",getalA,"in: ")
	getalB = int(input())
	if getalB <= 0:
		print("Geef enkel positieve getallen op. ")
		break
	som = som + getalB
		
	if getalA == 6:
		break

	getalA += 1
print("De totale som van de",getalA-1,"getallen is: ",som,"")
