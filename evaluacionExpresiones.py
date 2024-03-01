>>> 2 + 3                                   # Respuesta: tipo int, valor 5
>>> 4 / 0                                   # Respuesta: error de división por cero
>>> 5 + 3 * 2                               # Respuesta: tipo int, valor 11
>>> '5' + '3' * 2                           # Respuesta: tipo str, valor 533
>>> 2 ** 10 == 1000 or 2 ** 7 == 100        # Respuesta: tipo boleano, valor False
>>> int("cuarenta")                         # Respuesta: error al intentar tomar el valor entero de un str
>>> 70/16 + 100/24                          # Respuesta: tipo float, valor 8.54
>>> 200 + 19%                               # Respuesta: error por usar ( % ) como porcentaje
>>> 3 < (1024 % 10) < 6                     # Respuesta: tipo boleano, valor False
>>> 'six' + 'eight'                         # Respuesta: tipo str, valor "sixeight"
>>> 'six' * 'eight'                         # Respuesta: error al multiplicar un str con otro str
>>> float(-int('5') + int('10'))            # Respuesta: error al intentar sacar la parte entera de un str
>>> abs(len('ocho') - len('cinco'))         # Respuesta: tipo int, valor 1
>>> bool(14) or bool(-20)                   # Respuesta: tipo boleano, valor True
>>> float(str(int('5' * 4) / 3)[2])         # Respuesta: tipo float, valor 5.0