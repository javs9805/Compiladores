import sys

def lista():
	
    global entrada, caracter
    
    if ( caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9"):
		
        nroInvx = nroInv()
        listaX = lista()
		
        return nroInvx+listaX
    else:
        match(" ")
        return " "

def nroInv():
	
    global entrada, caracter

    digitoX = digito()
    Rx = R()

    return Rx+digitoX
	
def R():
	
    global entrada, caracter

    if ( caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9"):
		
        nroInvx = nroInv()

        return nroInvx
    else:
        match(" ")
        return " "


def digito():
      
    global caracter, entrada

    if( caracter == "0"):
          match("0")
          return "0"
    elif ( caracter == "1" ):
          match("1")
          return "1"
    elif ( caracter == "2" ):
          match("2")
          return "2"
    elif ( caracter == "3" ):
          match("3")
          return "3"
    elif ( caracter == "4" ):
          match("4")
          return "4"
    elif ( caracter == "5" ):
          match("5")
          return "5"
    elif ( caracter == "6" ):
          match("6")
          return "6"
    elif ( caracter == "7" ):
          match("7")
          return "7"
    elif ( caracter == "8" ):
          match("8")
          return "8"
    else:
          match("9")
          return "9"

def match(t):
	
    global caracter
    global entrada
    
    print(t,caracter)
    if ( t == caracter):
         entrada = entrada[1:]
         caracter = entrada[0:1]
         while( caracter == " "):
            entrada = entrada[1:]
            caracter = entrada[0:1]  
    else:
         print("Error!, {} no es una entrada valida!".format(caracter))
         exit(200)
             
             


#Programa principal
if __name__ == "__main__":
	
	#	print(lista())

	entrada = "987 654 321"
	caracter = entrada[0:1]

	print(lista())
