c = 0
result = []

while c == 0:
    n = int(input("Ingrese tiempo en minutos del trayecto: "))
    if n > 0:
        result.append(n)
    else:
        c += 1
        
c = 0
cantidad = len(result) - 1
total = 0

while cantidad > -1:
    total += result[cantidad]
    cantidad -= 1
    
horas = int(total / 60)
minutos = total % 60
print(f"""Total de minutos: {total}, esto en horas es igual a: {horas}:{minutos}""")