# MODULE BASIS PROGRAMMEREN
# INDIVIDUELE OEFENINGEN
# OEFENING 1
# CURSIST: JONAS LANCKMAN
# SEQUENTIE EN SELECTIE
# DATATYPES : CHAR, STRING, INTEGER

# Om deel te nemen aan de Lotto moet je minimum 18 jaar oud zijn.
# Ontwerp een consoletoepassing waarmee je de leeftijd van de gebruiker vraagt
# Wanneer de ingevoerde leeftijd minimum 18 jaar bedraagt, krijgt de gebruiker toegang tot de site van de Lotto en verschijnt de tekst :"Je bent x jaar oud. Je mag deelnemen aan de spelen".
# Indien niet voldaan aan deze voorwaarden verschijnt de tekst: "Je moet minimum 18 zijn."


minLeeftijd = 18
huidigeLeeftijd = int(input ("Voer leeftijd in: "))
if (huidigeLeeftijd >= 18):
	print ( "Je bent " + str(huidigeLeeftijd)  + " jaar oud. Je mag deelnemen aan de spelen")

else: 
	print ("Je moet minimum 18 zijn.")	