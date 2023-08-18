#6.	Si tienes una panadería que vende el mismo tipo de pan a $2500 10 veces al día, ¿cuánto venderá en una semana?
def punto6():
    precioPan = 2500
    cantidadDiaria = 10
    diasSemana = 7

    totalSemana = precioPan * cantidadDiaria * diasSemana

    print("La panadería venderá ${:,} en una semana.".format(totalSemana))


