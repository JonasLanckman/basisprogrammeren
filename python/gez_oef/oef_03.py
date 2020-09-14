# MODULE BASIS PROGRAMMEREN
# OEFENING 2
# CURSIST: JONAS LANCKMAN
# SEQUENTIE EN SELECTIE
# DATATYPES : CHAR, STRING, INTEGER
# De gebruiker dient een geboortejaar in te geven
# De gebruiker dient ook het huidige jaar in te geven
# Wanneer het verschil tussen het huidige jaar en geboortejaar groter is of gelijk is aan 18 = "Vanaf nu mag en kan alles, binnen de wettelijke grenzen"
# In de andere gevallen: "Mijn ouders regelen alles"

# VARIBALEN 
# minGeboortejaar = 2002
# maxHuidigjaar = 2020

minLeeftijd = 18
geboorteJaar = int(input ("Geef uw geboortejaar:"))
huidigJaar = int(input ("Geef het huidige jaar op:"))
verschil = huidigJaar - geboorteJaar

if (verschil < 0):
	print ("Het huidige jaar mag niet kleiner zijn dan het geboortejaar")

elif (verschil >= 18):
	print ("Vanaf nu kan en mag alles")
elif (verschil >= 20):
	print ("Groter dan 20")
else: 
	print ("Mijn ouders regelen alles")
