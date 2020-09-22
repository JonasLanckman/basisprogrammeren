

som = 0
teller = 1
y = 0
z = 0
for x in range(0,1000):
	print("Geef getal",x+1,"in: ")
	getalB = int(input())
	if (getalB > 0):
		z = z + teller


	if (getalB < 0):
		y = y + teller
	if (getalB == 0):
		break






print("Er zijn" ,z, "positieve getallen")
print("Er zijn" ,y, "negatieve getallen")