lista = []

n1 = int(input("Ingrese primer numero: "))
lista.append(n1)

o = input("Ingrese operador: ")
lista.append(o)

n2 = int(input("Ingrese segundo numero: "))
lista.append(n2)


op1 = lista[0]
op2 = lista[2]
ope = lista[1]

if ope == "+":
    result = op1 + op2
    
if ope == "-":
    result = op1 - op2
    
if ope == "*":
    result = op1 * op2
    
if ope == "/":
    result = op1 / op2
    
if ope == "**":
    result = op1 ** op2

print(f"""{op1} {ope} {op2} = {result}""")