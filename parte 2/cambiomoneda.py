tasas_de_cambio = {
    'USD': 1.0,  # Dólar estadounidense
    'EUR': 0.85,  # Euro
    'GBP': 0.77,  # Libra esterlina
    'JPY': 110.15,  # Yen japonés
    'CAD': 1.21  # Dólar canadiense
}


def convertir_moneda(monto, moneda_origen, moneda_destino):
    if moneda_origen in tasas_de_cambio and moneda_destino in tasas_de_cambio:
        tasa_origen = tasas_de_cambio[moneda_origen]
        tasa_destino = tasas_de_cambio[moneda_destino]
        monto_convertido = monto / tasa_origen * tasa_destino
        return monto_convertido
    else:
        return None

def main():
    print("Bienvenido al convertidor de moneda")
    print("Las monedas disponibles son: USD, EUR, GBP, JPY, CAD")

    while True:
        monto = float(input("Ingrese el monto a convertir: "))
        moneda_origen = input("Ingrese la moneda de origen (ej. USD): ").upper()
        moneda_destino = input("Ingrese la moneda de destino (ej. EUR): ").upper()

        if moneda_origen not in tasas_de_cambio or moneda_destino not in tasas_de_cambio:
            print("Moneda no válida. Por favor ingrese una moneda válida.")
            continue

        resultado = convertir_moneda(monto, moneda_origen, moneda_destino)

        if resultado is not None:
            print(f"{monto} {moneda_origen} equivale a {resultado:.2f} {moneda_destino}") # el :.2f hace que tenga 2 decimales
        else:
            print("No se pudo realizar la conversión. Por favor verifique las monedas ingresadas.")

        continuar = input("¿Desea realizar otra conversión? (s/n): ")
        if continuar.lower() != 's':
            break


if __name__ == "__main__":
    main()
