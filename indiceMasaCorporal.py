edad = input("Tiene 45 o mas años? (si/no): ")

if edad.lower() == "si":
    estatura = float(input("Ingrese su altura en metros: "))
    peso = float(input("Ingrese su peso en KG: "))
    imc = peso / (estatura**2)
    if imc < 22:
        print("Tu IMC es medio, con un valor de", imc)
    else:
        print("Tu IMC es alto, con un valor de", imc)

else:
    estatura = float(input("Ingrese su altura en metros: "))
    peso = float(input("Ingrese su peso en KG: "))
    imc = peso / (estatura**2)
    if imc < 22:
        print("Tu IMC es bajo, con un valor de", imc)
    else:
        print("Tu IMC es medio, con un valor de", imc)