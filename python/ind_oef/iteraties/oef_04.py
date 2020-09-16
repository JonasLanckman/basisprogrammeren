

# OM PER TWEE OMHOOG TE GAAN IN DE LIJST ZET JE IN DE RANGE
# NA DE 100 EEN 2


reeks = ""

for x in range(0,100):
	if (x < 10):
		reeks = reeks + "0" + str(x) + ","
	else:
		reeks = reeks + str(x) + ","
	
		
print(reeks[:-1])