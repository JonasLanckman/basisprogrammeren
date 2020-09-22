

# eindGetal = int(input("Geef het eindgetal in: "))
# afdrukOpScherm = ""

# for x in range(1, eindGetal,1):
# 	eindGetal = eindGetal + x 
# 	afdrukOpScherm = afdrukOpScherm + str(x) + ","



# print(afdrukOpScherm +str(x+1) + str(eindGetal))



test =1
teller = 1

getal = int(input("Geef getal in: "))
afdrukOpScherm = ""

while (teller <= getal):
	
	afdrukOpScherm+= str(test)+","
	
	test = test + teller
	teller = teller+1

		
print(afdrukOpScherm)

