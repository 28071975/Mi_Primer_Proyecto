# calculadora.py
# Script básico para operaciones matemáticas
numero_1 = float(input("primer número"))
numero_2 =float(input("segundo número"))
operacion = input("operación (+, -, *, /): ")

if operacion == '+':
    print("Resultado:", numero_1 + numero_2)
elif operacion == '-':
    print("Resultado:", numero_1 - numero_2)
elif operacion == '*':
    print("Resultado", numero_1 * numero_2)
