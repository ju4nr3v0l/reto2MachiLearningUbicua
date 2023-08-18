#El punto 7 del reto 2 variante 4 es el mismo ejercicio 3 del reto 2 variante 4
import punto1
import punto2
import punto3
import punto4
import punto5
import punto6


def mostrar_menu():
    print("Menú:")
    print("1. Punto 1 - Registrar un usuiario en el sistema")
    print("2. Punto 2 - Realizar la operacion ((numero * numero) + (2 * numero)) / 2")
    print("3. Punto 3 - Largo de una cadena de texto")
    print("4. Punto 4 - Eliminar los primeros 3 caracteres de una cadena de texto")
    print("5. Punto 5 - Eliminar los primeros 2 caracteres y los 2 ultimos de una cadena de texto")
    print("6. Punto 6 - Calculo de ventas semanales")
    print("0. Salir")
    print()



while True:
    mostrar_menu()
    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        punto1.punto1()
    elif opcion == "2":
        punto2.punto2()
    elif opcion == "3":
        punto3.punto3()
    elif opcion == "4":
        punto4.punto4()
    elif opcion == "5":
        punto5.punto5()
    elif opcion == "6":
        punto6.punto6()
    elif opcion == "0":
        print("Saliendo del programa.")
        break
    else:
        print("Opcion mp disponile. Por favor, seleccione una opcion de las listadas anteriormente.")


