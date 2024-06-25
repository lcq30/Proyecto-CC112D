import random


def jugar_adivina_numero():
    print("Bienvenido al juego Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100. Intenta adivinarlo.")

    numero_secreto = random.randint(1, 100) #creamos el numero aleatorio
    intentos = 0

    while True:
        intentos += 1
        try:
            guess = int(input("Ingresa tu número (o '0' para salir): "))
        except ValueError:
            print("Por favor ingresa un número válido.")
            continue

        if guess == 0:
            print("Has decidido salir del juego. El número secreto era", numero_secreto)
            break
        elif guess < 1 or guess > 100:
            print("El número debe estar entre 1 y 100.")
        elif guess < numero_secreto:
            print("El número secreto es mayor. Intenta de nuevo.")
        elif guess > numero_secreto:
            print("El número secreto es menor. Intenta de nuevo.")
        else:
            print(f"Felicidades! Adivinaste el número secreto {numero_secreto} en {intentos} intentos.")
            break

jugar_adivina_numero()
