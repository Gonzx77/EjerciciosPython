a = int(input("Ingrese a: "))
b = int(input("Ingrese b: "))
c = int(input("Ingrese c: "))

if a < b + c and b < a + c and c < a + b:
    if a == b and a == c and b == c:
        print("Es un triangulo equilatero")
    elif a == b or a == c or b == c:
        print("Es un triangulo isoceles")
    elif a != b and a != c and b != c:
        print("Es un triangulo escaleno")
else:
    print("Este triangulo no existe")