import sys

entrada = ""
caracter = ""


def R():
	global i

	if (caracter == " "):
		
		match(" ")

		x = lista()

		return x

	else:
		return " "


def lista():

	global i

	nroInvX = nroInv()
	Rx = R()

	return nroInvX + Rx


def nroInv():

	global i

	digitoX = digito()
	R1x = R1()

	x = R1x + digitoX

	return x


def R1():

	global i

	if (caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3"
	    or caracter == "4" or caracter == "5" or caracter == "6"
	    or caracter == "7" or caracter == "8" or caracter == "9"):
		nroInvx = nroInv()
		return nroInvx
	else:
		if( caracter == " "):
			print("Entro al if, caracter == "+caracter)
			return " "
		else:
			match(" ")
	


def digito():

	global caracter

	if (caracter == "0"):
		match("0")
		return "0"
	elif (caracter == "1"):
		match("1")
		return "1"
	elif (caracter == "2"):
		match("2")
		return "2"
	elif (caracter == "3"):
		match("3")
		return "3"
	elif (caracter == "4"):
		match("4")
		return "4"
	elif (caracter == "5"):
		match("5")
		return "5"
	elif (caracter == "6"):
		match("6")
		return "6"
	elif (caracter == "7"):
		match("7")
		return "7"
	elif (caracter == "8"):
		match("8")
		return "8"
	else:
		match("9")
		return "9"


def espacio():

	global caracter

	match(" ")


"""
def match(t):
	global caracter
	global entrada
	print(caracter + t)
	if (t == caracter):
		entrada = entrada[1:]
		caracter = entrada[0:1]
		if t == " ":
			while (caracter == " "):
				entrada = entrada[1:]
				caracter = entrada[0:1]
	else:
		if t == " ":
			while (caracter == " "):
				entrada = entrada[1:]
				caracter = entrada[0:1]
		
		print("Error!, {} no es una entrada valida!".format(caracter))
		sys.exit(200)
		return

"""

def match(t):
	global caracter
	global entrada

	if( t == caracter):
		entrada = entrada[1:]
		caracter = entrada[0:1]
		
		print(caracter)

		#while( caracter == " "):
		#	entrada = entrada[1:]
		#	caracter = entrada[0:1]
	else:
		print("Error!, {} no es una entrada valida!".format(caracter))
		sys.exit(200)

#Programa principal
if __name__ == "__main__":
	
	#	print(lista())

	#entrada = "987 654 321"
	
	entrada = "987 54 654"

	
	caracter = entrada[0:1]

	print(lista())
