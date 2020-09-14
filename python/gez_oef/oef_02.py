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

geboorteJaar = int(input ("Geef uw geboortejaar:"))
huidigJaar = int(input ("Geef het huidige jaar op:"))
#verschil = huidigeJaar - geboorteJaar

if ((huidigJaar - geboorteJaar) >= 18):
	print ("Vanaf nu mag en kan alles, binnen de wettelijke grenzen")

else: 
	print ("Mijn ouders regelen alles")
