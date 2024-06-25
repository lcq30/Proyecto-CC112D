import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-3.5, 3.5, 400)
seno = np.sin(x)
coseno = np.cos(x)
fig, ax = plt.subplots()
ax.plot(x, seno, color='red', label='Seno')
ax.plot(x, coseno, color='#165181', label='Coseno')
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-1.2, 1.2)
ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
ax.set_yticks(np.arange(-1, 1.1, 0.5))
ax.set_xticklabels(['$-\pi$', r'$-\frac{\pi}{2}$', '0', r'$\frac{\pi}{2}$', r'$\pi$'])
ax.set_yticklabels(['-1.0', '-0.5', '0', '0.5', '1.0'])
#agregamos leyendas
ax.legend()
ax.text(-3, 0.75, 'Seno', color='red', fontsize=12, ha='left', va='center')
ax.text(-3, -0.75, 'Coseno', color='#165181', fontsize=12, ha='left', va='center')
plt.show()
