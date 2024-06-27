import numpy as np
#creo una matriz
matriz = np.array([[ 0,  1,  2,  3],
                   [ 4,  5,  6,  7],
                   [ 8,  9, 10, 11]])

print("Matriz original:")
print(matriz)
print()
submatriz = matriz[:2, 1:3]

print("Submatriz extraída (primeras 2 filas y columnas 1 y 2):")
print(submatriz)
print()
submatriz[0, 0] = 99

print("Submatriz después de modificar submatriz[0, 0] a 99:")
print(submatriz)
print()
print("Matriz original después de modificar la submatriz:")
print(matriz)
