agenda = {}

def agregar():
    nombre = input("Ingresa el nombre del contacto: ")
    telefono = input("Ingresa el número de teléfono del contacto: ")
    agenda[nombre] = telefono
    print(f"Contacto '{nombre}' agregado correctamente.")

def buscar():
    nombre = input("Ingresa el nombre del contacto que deseas buscar: ")
    if nombre in agenda:
        print(f"Nombre: {nombre} - Teléfono: {agenda[nombre]}")
    else:
        print(f"El contacto '{nombre}' no está en la agenda.")

def mostrar():
    print("Agenda Telefónica:")
    for nombre, telefono in agenda.items():
        print(f"Nombre: {nombre} - Teléfono: {telefono}")

while True:
    print("\n1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Mostrar agenda")
    print("4. Salir")
    opcion = input("Selecciona una opción : ")

    if opcion == '1':
        agregar()
    elif opcion == '2':
        buscar()
    elif opcion == '3':
        mostrar()
    elif opcion == '4':
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida. Por favor, selecciona una opción válida .")
