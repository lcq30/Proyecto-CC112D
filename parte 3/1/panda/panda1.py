'''
ejercicio:
¿Qué produce df.iloc[0:3, 0:3] ?
selecciona las filas y columnas de 0 hasta 3 dentro del dataframe

'''
#Ejercicio
'''
Agrega las columnas siguientes: edad_mas_5, nombre_completo y genero
edad_mas_5viene de sumar 5 a la etiqueta edad
nombre_completo viene de sumar las etiquetas primer_nombre, _ y ultimo_nombre
genero es una serie de elementos 'F','F','M','M','M','F'.
'''
import pandas as pd

data1 = {
    'primer_nombre': ['Amy', 'Amy', 'Jason', 'Nick', 'Stephen', 'Amy'],
    'ultimo_nombre': ['Jackson', 'J', 'Miller', 'Milner', 'L', 'J'],
    'edad': [42, 42, 36, 24, 24, 42]
}
#creo un dataframe de pandas a partir de los datos de data1
df = pd.DataFrame(data1, columns=['primer_nombre', 'ultimo_nombre', 'edad'])

df['edad_mas_5'] = df['edad'] + 5

df['nombre_completo'] = df['primer_nombre'] + ' ' + df['ultimo_nombre'].replace('J', '')

genero = ['F', 'F', 'M', 'M', 'M', 'F']
df['genero'] = genero

# Mostrar el DataFrame resultante
print(df)
