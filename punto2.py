#2.	Utilizando Python, dado un número n calcula la siguiente operación  ((numero * numero) + (2 * numero)) / 2
# e imprime en pantalla el resultado:
# Output: El resultado de la operación es
def punto2():
    try:
     numero = int(input("Digite un numero entero: "))
     resultado = ((numero * numero) + (2 * numero)) / 2
     print("El resultado de la operación es " + str(resultado))
    except:
     print("El dato ingresado no es un numero o no es un numero entero")