from calculadora import *

print("Bienvenido a la calculadora")

operacion = oper1 = oper2 = "None"

while operacion not in ("+","-", "*", "/") :
    operacion=input("Indique la operación (+, -, *, /): ")

while not str(oper1).isnumeric() :
    oper1=input("Indique el primer número: ")
oper1 = int(oper1)

while not str(oper2).isnumeric() :
    oper2=input("Indique el segundo número: ")
oper2 = int(oper2)

if operacion == "+" :
    print("El resultado de la suma es:", suma(oper1, oper2))
elif operacion == "-" :
    print("El resultado de la resta es:", resta(oper1, oper2))
elif operacion == "*" :
    print("El resultado de la multiplicación es:", multiplicacion(oper1, oper2))
elif operacion == "/" :
    print("El resultado de la división es:", division(oper1, oper2))
