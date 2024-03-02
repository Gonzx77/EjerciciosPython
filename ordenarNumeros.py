c = 0
lista = []

while c == 0:
    Num = int(input("Ingrese un numero: "))
    op = input("Desea agregar mas numeros? (si / no): ")
    lista.append(Num)
    if op.lower() == "si":
        print("ok")
    else:
        print("ok")
        c += 1

lista.sort()
print(lista)