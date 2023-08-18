#3.	Escribe un programa que imprima en pantalla el largo de una cadena de texto:

#Input: Ingrese una cadena de texto: ¡Hola mundo!
#Output: La cadena de texto tiene 12 caracteres

def punto3():
    cadenaDeTexto = input("Ingrese una cadena de texto: ")
    longitud = len(cadenaDeTexto)
    print("La cadena de texto tiene " + str(longitud) + " caracteres de longitud")