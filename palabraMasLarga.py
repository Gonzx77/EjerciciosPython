palabra1 = input("Ingrese una palabra: ")
palabra2 = input("Ingrese otra palabra: ")

c1 = len(palabra1)
c2 = len(palabra2)

if c1 > c2:
    print(f"""El orden segun su cantidad de caracteres correcto es: {palabra1}, {palabra2}""")
else:
    print(f"""El orden segun su cantidad de caracteres correcto es: {palabra2}, {palabra1}""")