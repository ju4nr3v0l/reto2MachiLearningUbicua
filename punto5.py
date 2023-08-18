#5.	Escribe un programa que elimine los primeros dos y los últimos dos caracteres de una cadena de texto:

#Input: Ingrese una cadena de texto: Hola mundo
#Output: la mun

def punto5():
    cadenaDeTexto = input("Ingrese una cadena de texto: ")

    if len(cadenaDeTexto) >= 4:
        nuevaCadenaDeTexto = cadenaDeTexto[2:-2]
        print("Output:", nuevaCadenaDeTexto)
    else:
        print("La cadena es demasiado corta para realizar la operación.")