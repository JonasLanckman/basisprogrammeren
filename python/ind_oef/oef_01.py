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

 # Wanneer men 18 jaar of ouder is dient men te vragen of ze een volledige bulletin van 12 vakjes willen spelen.
 # Bij een volledige bulletin toon je de kostprijs van 20 euro. 
 # Voor 2 vakjes is de kostprijs 4 euro. 
 # Voor 4 vakjes 8 euro. Voor 6 vakjes 12 euro. 
 # Voor 10 vakjes 18 euro.


minLeeftijd = 18
huidigeLeeftijd = int(input ("Voer leeftijd in: "))
if (huidigeLeeftijd >= 18):
	
			antwoordA = (input ("Wilt u een volledige bulletin spelen van 12 vakjes? J/N:" ))
			if (antwoordA == "J"):
				print ("Een volledige bulletin van 12 vakjes kost: 20 euro")
			else:
				aantalVakjes = int(input ("Geef het aantal vakjes op. Kiezen tussen: 2,4,6 of 10:"))
				if (aantalVakjes == 2):
					print ("Kostprijs is 4 euro")
				elif (aantalVakjes == 4):
					print ("Kostprijs is 8 euro")
				elif (aantalVakjes == 6):
					print ("Kostprijs is 12 euro")
				else:
					print ("Kostprijs is 18 euro")




else: 
	print ("Je moet minimum 18 zijn.")	
