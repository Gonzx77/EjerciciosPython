edad = int(input("Ingrese su edad: "))
peso = float(input("Ingrese su peso en KG: "))
estatura = float(input("Ingrese su altura en Mtrs: "))

imc = peso / (estatura**2)
print(imc)

if edad < 45:
    if imc < 22:
        print("Tu imc es bajo")
    elif imc >= 22:
        print("Tu imc es medio")
        
elif edad >= 45:
    if imc < 22:
        print("Tu imc es medio")
    elif imc >= 22:
        print("Tu imc es alto")