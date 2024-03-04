n1 = int(input("Ingrese numero 1: "))
n2 = int(input("Ingrese numero 2: "))

if n1 < n2:
    x = n1 + 1
    resultado = 0
    while x < n2:
        resultado += x
        x += 1

print(resultado)