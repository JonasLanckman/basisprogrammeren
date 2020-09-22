
letter = ""
eindLetter = ord(input ("Geef je eindletter in: "))

for x in range(65,eindLetter+1)[::-1]:
	print(chr(x))








for x in range (65, eindLetter):
	letter = letter[:-1]
	print(letter)