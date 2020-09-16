

# VARIABELEN
ster = "*"


aantalLijnen = int(input("Geef een even aantal lijnen op: "))
print(ster)
for x in range(1 , aantalLijnen):
	ster = ster + "*"
	print(ster)
for x in range (1, aantalLijnen):
	ster = ster[:-1]
	print(ster)