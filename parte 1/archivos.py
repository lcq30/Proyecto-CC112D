def copiar_archivo(origen, destino):
    try:
        with open(origen, 'r') as archivo_origen:
            contenido = archivo_origen.read()
        with open(destino, 'w') as archivo_destino:
            archivo_destino.write(contenido)
        print("El contenido del archivo se ha copiado correctamente.")
    except FileNotFoundError:
        print("Error: No se pudo encontrar el archivo.")
    except IOError:
        print("Error: Ocurrió un error al leer o escribir el archivo.")

copiar_archivo('archivo1.txt', 'archivo2.txt')
