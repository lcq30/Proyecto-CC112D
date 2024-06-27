import pandas as pd
import numpy as np

df = pd.DataFrame({'Nombre': ['jack', 'jane', 'jack', 'jane', 'jack', 'jane', 'jack', 'jane'],
                   'Estado': ['SFO', 'SFO', 'NYK', 'CA', 'NYK', 'NYK', 'SFO', 'CA'],
                   'Genero': ['A', 'A', 'B', 'A', 'C', 'B', 'C', 'A'],
                   'Edad': np.random.uniform(24, 50, size=8),
                   'Salario': np.random.uniform(3000, 5000, size=8)})

suma_por_nombres = df.groupby('Nombre').sum()
#se está utilizando el método groupby de pandas para agrupar los datos del DataFrame df
#por la columna 'Nombre'. Después, se aplica el método sum() sobre los grupos resultantes.

print("Suma por nombres:")
print(suma_por_nombres)
print()
agregaciones = {
    'Edad': ['max'],
    'Salario': ['max']
}
maximos_por_nombre_estado = df.groupby(['Nombre', 'Estado']).agg(agregaciones)

print("Edad máxima y salario máximo por nombre/estado:")
print(maximos_por_nombre_estado)
