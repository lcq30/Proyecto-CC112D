import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(start=-2, stop=2, num=400)
fig, ax = plt.subplots(figsize=(10, 6))
for N in range(1, 11):
    #establesco "colores"
    ax.plot(x, x**N, label=f'x^{N}')
ax.set_title(r'$x$ hasta $N$, donde $N=1,\ldots,10$')
ax.legend()
plt.grid(True)
plt.show()
