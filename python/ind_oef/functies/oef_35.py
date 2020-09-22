
def palindroom(s):
	return s == s[::-1]

s = input("Geef een woord in: ")
antwoord = palindroom(s)

if antwoord:
	print("Dit is een palindroom")
else:
	print("Dit is geen palindroom")