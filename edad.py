from datetime import datetime

fecha_actual = datetime.now()


dia = int(input("Ingrese día de nacimiento: "))
mes = int(input("Ingrese mes de nacimiento: "))
año = int(input("Ingrese año de nacimiento: "))
fecha_nacimiento = datetime(año, mes, dia)

diferencia = fecha_actual - fecha_nacimiento

edad = diferencia.days // 365

print("Tienes", edad, "años.")