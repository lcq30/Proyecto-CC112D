import matplotlib.pyplot as plt
import numpy as np
# creo arreglo de valores numericos
x = np.linspace(start=-5, stop=5, num=150)
# creo una figura que contiene un arreglo de subplots
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

axs[0, 0].plot(x, x, label='Lineal')
axs[0, 0].set_title('Función Lineal')
axs[0, 1].plot(x, x**2, label='Cuadrático')
axs[0, 1].set_title('Función Cuadrática')
axs[1, 0].plot(x, x**3, label='Cúbico')
axs[1, 0].set_title('Función Cúbica')
axs[1, 1].plot(x, x**4, label='4ta Potencia')
axs[1, 1].set_title('Función 4ta Potencia')

# Ajustar espacio ente subplots
plt.tight_layout()
for ax in axs.flat:
    ax.legend()  # se muestran las leyendas

plt.show()
