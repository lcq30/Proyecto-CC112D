import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3.5, 3.5, 400)
seno = np.sin(x)
coseno = np.cos(x)

fig, ax = plt.subplots()
ax.plot(x, seno, color='green', label='Seno')
ax.plot(x, coseno, color='#341161', label='Coseno')
ax.set_xlim(-3.5, 3.5)
ax.set_ylim(-1.2, 1.2)

ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
ax.set_yticks([-1, 0, 1])

ax.set_xticklabels([r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'], size=17)
ax.set_yticklabels(['-1', '0', '+1'], size=17)
ax.legend(loc='upper left')
ax.text(-0.25, 0, '(0,0)')
ax.text(np.pi - 0.25, 0, r'$(\pi,0)$', size=15)
ax.annotate('Origen', xy=(0, 0), xytext=(1, -0.7), arrowprops=dict(facecolor='blue'))
plt.show()
