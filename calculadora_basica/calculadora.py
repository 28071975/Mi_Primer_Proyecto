# calculadora.py
#nueva versión de la calculadora para el nuevo upload


def pedir_numero(mensaje):
    while True:
        valor = input(mensaje)
        try:
            return float(valor)
        except ValueError:
            print("❌ Error: introduce un número válido.")

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        print("❌ Error: no se puede dividir por cero.")
        return None
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a):
    if a < 0:
        print("❌ Error: no se puede calcular la raíz de un número negativo.")
        return None
    return a ** 0.5

def mostrar_menu():
    print("\n===============================")
    print("      CALCULADORA PYTHON")
    print("===============================")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. Raíz cuadrada")
    print("7. Ver historial")
    print("8. Salir")
    print("===============================")


historial = []

while True:
    mostrar_menu()
    opcion = input("Selecciona una opción (1-8): ")

    if opcion == "1":
        a = pedir_numero("Primer número: ")
        b = pedir_numero("Segundo número: ")
        resultado = sumar(a, b)
        print(f"✅ Resultado: {resultado}")
        historial.append(f"{a} + {b} = {resultado}")

    elif opcion == "2":
        a = pedir_numero("Primer número: ")
        b = pedir_numero("Segundo número: ")
        resultado = restar(a, b)
        print(f"✅ Resultado: {resultado}")
        historial.append(f"{a} - {b} = {resultado}")

    elif opcion == "3":
        a = pedir_numero("Primer número: ")
        b = pedir_numero("Segundo número: ")
        resultado = multiplicar(a, b)
        print(f"✅ Resultado: {resultado}")
        historial.append(f"{a} * {b} = {resultado}")

    elif opcion == "4":
        a = pedir_numero("Dividendo: ")
        b = pedir_numero("Divisor: ")
        resultado = dividir(a, b)
        if resultado is not None:
            print(f"✅ Resultado: {resultado}")
            historial.append(f"{a} / {b} = {resultado}")

    elif opcion == "5":
        a = pedir_numero("Base: ")
        b = pedir_numero("Exponente: ")
        resultado = potencia(a, b)
        print(f"✅ Resultado: {resultado}")
        historial.append(f"{a} ^ {b} = {resultado}")

    elif opcion == "6":
        a = pedir_numero("Número: ")
        resultado = raiz(a)
        if resultado is not None:
            print(f"✅ Resultado: {resultado}")
            historial.append(f"√{a} = {resultado}")

    elif opcion == "7":
        if len(historial) == 0:
            print("📜 No hay operaciones registradas.")
        else:
            print("\n📜 HISTORIAL DE OPERACIONES:")
            for i, op in enumerate(historial, start=1):
                print(f"{i}. {op}")

    elif opcion == "8":
        print("👋 Gracias por usar la calculadora. ¡Hasta luego!")
        break

    else:
        print("⚠️  Opción inválida. Intenta de nuevo.")
