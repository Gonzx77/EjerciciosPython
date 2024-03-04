def verificar_set(marcador):
    juegosjugador1, juegosjugador2 = map(int, marcador.split("-"))
    
    if juegosjugador1 < 0 or juegosjugador2 < 0:
        return "El marcador es inválido"

    if juegosjugador1 >= 6 and juegosjugador1 >= juegosjugador2 + 2:
        return "El jugador 1 ganó el set"
    elif juegosjugador2 >= 6 and juegosjugador2 >= juegosjugador1 + 2:
        return "El jugador 2 ganó el set"
    
    if juegosjugador1 == 5 and juegosjugador2 == 5:
        return "El set está empatado a 5-5"
    
    if juegosjugador1 == juegosjugador2 == 6:
        return "El set está empatado a 6-6"
    
    return "El set aún no ha terminado"


marcador_set = input("Ingrese el marcador del set (en el formato 'juegos_jugador1-juegos_jugador2'): ")
resultado = verificar_set(marcador_set)
print(resultado)