N1 = int(input("Ingrese su nota del certamen 1: "))
N2 = int(input("Ingrese su nota del certamen 2: "))
Lab = int(input("Ingrese su nota del laboratorio: "))

N3 = 0
NF = 0

while NF < 60:
    NC = (N1 + N2 + N3) / 3
    NF = (NC * 0.7) + (Lab * 0.3)
    
    N3 += 1
    
print(f"""Debe sacar una nota minima de {N3} en el certamen 3 para aprobar""")