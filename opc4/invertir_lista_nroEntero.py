
"""
        Traductor Dirigido por la Sintexis
         
        Recibe una lista de números enteros y retorna la misma lista pero esta vez con los números invertidos.
        
        Ejemplo:
	        - Entrada = 43 2451 701
	        - Salida = 34 1542 107

        Autores: Cesar Belotto y Javier Lopez
"""

import sys


"""
lista → + nro lista | - nro lista | nro lista | ε
"""
def lista():

    global caracter

    if( caracter == "+"):
        match("+")
        nroX = nro()
        listaX = lista()
        x = "+"+nroX+" "+listaX
        return x  
    
    elif ( caracter == "-"):
        match("-")
        nroX = nro()
        listaX = lista()
        x = "-"+nroX+" "+listaX
        return x
    
    elif ( caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9"):
        nroX = nro()
        listaX = lista()
        x = nroX+" "+listaX
        return x
    
    else:
        match(" ")
        return ""        

"""
nro → digito R
"""
def nro():

    digitoX = digito()
    Rx = R()
    x = Rx+digitoX

    return x

"""
R → nro | ε
"""
def R():

    global caracter

    if ( caracter == "0" or caracter == "1" or caracter == "2" or caracter == "3" or caracter == "4" or caracter == "5" or caracter == "6" or caracter == "7" or caracter == "8" or caracter == "9"):

        digitoX = digito()
        Rx = R()
        x = Rx+digitoX
        return x
    
    else:
        match(" ")
        return ""

"""
digito → 0 | 1 | … | 9
"""    
def digito():

    global caracter

    if ( caracter == "0" ):
        match("0")
        return "0"
    elif( caracter == "1" ):
        match("1")
        return "1"
    elif( caracter == "2" ):
        match("2")
        return "2"
    elif( caracter == "3" ):
        match("3")
        return "3"
    elif( caracter == "4" ):
        match("4")
        return "4"
    elif( caracter == "5" ):
        match("5")
        return "5"
    elif( caracter == "6" ):
        match("6")
        return "6"
    elif( caracter == "7" ):
        match("7")
        return "7"
    elif( caracter == "8" ):
        match("8")
        return "8"
    else:
        match("9")
        return "9"
    

def match(t):

    global caracter
    global entrada

    
    if( len(caracter) > 0):
        
        if ( t == caracter):

            entrada = entrada[1:]
            caracter = entrada[0:1]

            if(t == " "):
                while( caracter == " "):
                    entrada = entrada[1:]
                    caracter = entrada[0:1]
        else:

            print("Error!, {} no es una entrada valida!".format(caracter))
            exit(200)

#Progrma principal

#entrada = "43               +2451 *701            "
	
entrada = input("Ingrese la entrada: ")
    
caracter = entrada[0:1]

print("Entrada: "+entrada+"\nSalida: "+lista())