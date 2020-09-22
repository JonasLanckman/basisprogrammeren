

def schrikkeljaar(jaar):
	if jaar % 400 == 0:
		return True
	elif jaar % 100 == 0:
		return False
	elif jaar % 4 == 0:
		return True
	else:
		return False
jaartal = int(input("Geef een jaartal in: "))
if schrikkeljaar(jaartal) == True:
	print("Dit is een schrikkeljaar.")
else:
	print("Dit is geen schrikkeljaar.")