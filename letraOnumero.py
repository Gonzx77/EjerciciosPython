caracter = input("Ingresa caracter: ")

if caracter.isnumeric():
    print("El caracter", caracter, "es numerico.")
elif caracter.isalpha():
    if caracter == caracter.upper():
        print("El caracter", caracter, "es una letra mayuscula.")
    elif caracter == caracter.lower():
        print("El caracter", caracter, "es una letra minuscula.")
else:
    print("El caracter", caracter, "no es ni letra ni numero")