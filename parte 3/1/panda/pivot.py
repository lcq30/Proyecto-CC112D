import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Nombre': ['jack', 'jane', 'jack', 'jane', 'jack', 'jane', 'jack', 'jane'],
    'Estado': ['SFO', 'SFO', 'NYK', 'CA', 'NYK', 'NYK', 'SFO', 'CA'],
    'Edad': np.random.uniform(24, 50, size=8)
})

#df.groupby(['Estado', 'Nombre']) agupamos datos de variable estado y nombre
tabla_grupo = df.groupby(['Estado', 'Nombre'])['Edad'].mean().reset_index()
#mean() Esto calcula la media de las edades
#.reset_index() : Esto convierte los índices de los grupos (Estado y Nombre) en columnas regulares
#   y restablece el índice del DataFrame para que sea numérico, comenzando desde 0.

edad_media_estado = df.groupby('Estado')['Edad'].mean()

print("Edad media por Estado:")
print(edad_media_estado)
