import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3.5, 3.5, 400)
seno = np.sin(x)
coseno = np.cos(x)
fig, ax = plt.subplots()
#ponemos "colores"
ax.plot(x, seno, color='red', label='Seno')
ax.plot(x, coseno, color='#165181', label='Coseno')
#limites de eje
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-1.2, 1.2)
#establesco tiks
ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
ax.set_yticks(np.arange(-1, 1.1, 0.5))
ax.set_xticklabels(['$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$'])
ax.set_yticklabels(['-1.0', '-0.5', '0', '0.5', '1.0'])
ax.legend()
plt.show()
