#Escribe un programa en python que elimine los primeros tres caracteres de una cadena de texto:

#Input: Ingrese una cadena de texto: Hola mundo
#Output: a mundo

def punto4():
    cadenaDeTexto = input("Ingrese una cadena de texto: ")
    cadenaDeTexto = cadenaDeTexto[3:]
    print(cadenaDeTexto)