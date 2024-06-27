def sumar(a, b):
    return a + b
def restar(a, b):
    return a - b
def multiplicar(a, b):
    return a * b
def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: división por cero"
def calculadora():
    while True:
        print("\nCalculadora básica")
        print("Seleccione la operación:")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicación")
        print("4. División")
        print("5. Salir")

        opcion = input("Ingrese el número de la operación deseada: ")

        if opcion == '1':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = sumar(num1, num2)
            print(f"Resultado de la suma: {resultado}")

        elif opcion == '2':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = restar(num1, num2)
            print(f"Resultado de la resta: {resultado}")

        elif opcion == '3':
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = multiplicar(num1, num2)
            print(f"Resultado de la multiplicación: {resultado}")

        elif opcion == '4':
            num1 = float(input("Ingrese el numerador: "))
            num2 = float(input("Ingrese el denominador: "))
            resultado = dividir(num1, num2)
            print(f"Resultado de la división: {resultado}")

        elif opcion == '5':
            print("Saliendo de la calculadora...")
            break

        else:
            print("Opción no válida. Por favor ingrese un número del 1 al 5.")

calculadora()
