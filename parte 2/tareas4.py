def mostrar_menu():
    print("\n===== Lista de Tareas =====")
    print("1. Mostrar tareas")
    print("2. Agregar tarea")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")
    print("============================")

def mostrar_tareas(tareas):
    print("\n===== Tareas Pendientes =====")
    if not tareas:
        print("No hay tareas pendientes")
    else:
        for i, tarea in enumerate(tareas, 1):
            estado = "Completada" if tarea['completada'] else "Pendiente"
            print(f"{i}. [{estado}] {tarea['descripcion']}")
    print("============================")

def agregar_tarea(tareas):
    descripcion = input("Ingrese la descripción de la tarea: ")
    tarea = {'descripcion': descripcion, 'completada': False}
    tareas.append(tarea)
    print(f"Tarea '{descripcion}' agregada correctamente.")

def marcar_completada(tareas):
    mostrar_tareas(tareas)
    try:
        indice = int(input("Ingrese el número de la tarea que desea marcar como completada: ")) - 1
        if 0 <= indice < len(tareas):
            tareas[indice]['completada'] = True
            print(f"Tarea '{tareas[indice]['descripcion']}' marcada como completada.")
        else:
            print("Número de tarea fuera de rango.")
    except ValueError:
        print("Entrada no válida. Ingrese un número válido.")

def eliminar_tarea(tareas):
    mostrar_tareas(tareas)
    try:
        indice = int(input("Ingrese el número de la tarea que desea eliminar: ")) - 1
        if 0 <= indice < len(tareas):
            descripcion = tareas[indice]['descripcion']
            del tareas[indice]
            print(f"Tarea '{descripcion}' eliminada correctamente.")
        else:
            print("Número de tarea fuera de rango.")
    except ValueError:
        print("Entrada no válida. Ingrese un número válido.")

# Función principal para ejecutar la aplicación
def main():
    tareas = []
    while True:
        mostrar_menu()
        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == '1':
            mostrar_tareas(tareas)
        elif opcion == '2':
            agregar_tarea(tareas)
        elif opcion == '3':
            marcar_completada(tareas)
        elif opcion == '4':
            eliminar_tarea(tareas)
        elif opcion == '5':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor ingrese un número del 1 al 5.")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
