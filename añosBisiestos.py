# introducir un día adicional en los años divisibles por 4
# a partir de 1582 el último año de cada siglo dejaba de ser bisiesto, a no ser que fuera divisible por 400
# teniendo en cuenta cuál era el calendario vigente en ese año:

año = int(input("Ingrese el año que desea consultar: "))

if año < 1582:
    if año % 4 == 0:
        print(f"""El año {año} es un año bisiesto""")
    else:
        print(f"""El año {año} no es un año bisiesto""")

elif año >= 1582:
    ultimos_dos_digitos = año % 100
    if ultimos_dos_digitos == 0:
        if año % 400 == 0:
            print(f"""El año {año} es un año bisiesto""")
        else:
            print(f"""El año {año} no es un año bisiesto""")
    else:
        if año > 1582:
            if año % 4 == 0:
                print(f"""El año {año} es un año bisiesto""")
            else:
                print(f"""El año {año} no es un año bisiesto""")