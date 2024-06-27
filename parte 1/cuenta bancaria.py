class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad
            print(f"Depósito de {cantidad} realizado. Nuevo saldo: {self.saldo}")
        else:
            print("La cantidad a depositar debe ser mayor que cero.")

    def retirar(self, cantidad):
        if 0 < cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de {cantidad} realizado. Nuevo saldo: {self.saldo}")
        else:
            print("Fondos insuficientes o cantidad inválida para retirar.")

    def consultar_saldo(self):
        print(f"Saldo actual de la cuenta de {self.titular}: {self.saldo}")

def interactuar_con_cuenta(cuenta):
    while True:
        print("\n¿Qué desea hacer?")
        print("1. Consultar saldo")
        print("2. Depositar dinero")
        print("3. Retirar dinero")
        print("4. Salir")

        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == '1':
            cuenta.consultar_saldo()
        elif opcion == '2':
            cantidad = float(input("Ingrese la cantidad a depositar: "))
            cuenta.depositar(cantidad)
        elif opcion == '3':
            cantidad = float(input("Ingrese la cantidad a retirar: "))
            cuenta.retirar(cantidad)
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor ingrese un número del 1 al 4.")

titular = input("Ingrese el nombre del titular de la cuenta: ")
saldo1 = float(input("Ingrese el saldo inicial de la cuenta: "))

cuenta = CuentaBancaria(titular, saldo1)
interactuar_con_cuenta(cuenta)
