import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0, 50, 100)
y1 = np.sin(x)
y2 = np.cos(x)
fig, ax = plt.subplots()
ax.plot(x, y1, label='Seno')
ax.set_xlabel('Etiqueta x en los ejes', fontsize=12)
ax.set_ylabel('Etiqueta y en los ejes', fontsize=12)
ax.legend()
fig.tight_layout(pad=2.0)

# Mostrar el gráfico
plt.show()
