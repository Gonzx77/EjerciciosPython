n = float(input("Ingrese numero para hallar sus divisores enteros: "))

c = 1
result = []

while c < n:
    a = n % c
    if a == 0:
        result.append(c)
    c += 1
    
print(result)