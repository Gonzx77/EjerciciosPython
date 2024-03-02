dividendo = int(input("Ingrese dividendo: "))
divisor = int(input("Ingrese divisor: "))

cociente = dividendo / divisor
resto = dividendo % divisor  
cociente = int(cociente)

if resto == 0:
    print("La division es exacta")
    print("El cociente es:", cociente)
    print("El resto es:", resto)
else:
    print("La division no es exacta")
    print("El cociente es:", cociente)
    print("El resto es:", resto)