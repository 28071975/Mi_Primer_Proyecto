# calculadora.py
# Script básico para operaciones matemáticas

print("=== Calculadora básica ===")

try:
    numero_1 = float(input("Primer número: "))
    numero_2 = float(input("Segundo número: "))
    operacion = input("Operación (+, -, *, /): ")

    if operacion == '+':
        resultado = numero_1 + numero_2
        print("Resultado:", resultado)
    elif operacion == '-':
        resultado = numero_1 - numero_2
        print("Resultado:", resultado)
    elif operacion == '*':
        resultado = numero_1 * numero_2
        print("Resultado:", resultado)
    elif operacion == '/':
        if numero_2 == 0:
            print("Error: no se puede dividir entre cero.")
        else:
            resultado = numero_1 / numero_2
            print("Resultado:", resultado)
    else:
        print("Operación no válida. Usa +, -, * o /.")

except ValueError:
    print("Error: Debes ingresar solo números válidos.")
