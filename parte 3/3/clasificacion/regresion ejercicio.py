import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#ejemplo
data = {
    'nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Luis'],
    'ciudad': ['Madrid', 'Barcelona', 'Sevilla', 'Valencia', 'Bilbao'],
    'edad': [25, 30, 28, 35, 29],
    'saldo': [1000.50, 1500.75, 800.00, 1200.25, 900.50],
    'y': [0, 1, 0, 1, 0]  # Variable de respuesta binaria (0 o 1)
}

df = pd.DataFrame(data)
categoricas = ['nombre', 'ciudad']
numericas = ['edad', 'saldo']

# Separar las variables predictoras (X) y la variable objetivo (y)
X = df[categoricas + numericas]
y = df['y']

# Dividir datos en entrenamiento y validación
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=1)

#Codificación one-hot para variables categóricas
encoder = OneHotEncoder(sparse=False, handle_unknown='ignore')
encoder.fit(X_train[categoricas])

# Transformar datos de entrenamiento y validación
X_train_encoded = encoder.transform(X_train[categoricas])
X_val_encoded = encoder.transform(X_val[categoricas])

# Concatenar variables numéricas con variables codificadas
X_train_final = pd.DataFrame(X_train_encoded, columns=encoder.get_feature_names_out(categoricas))
X_val_final = pd.DataFrame(X_val_encoded, columns=encoder.get_feature_names_out(categoricas))
X_train_final[numericas] = X_train[numericas].reset_index(drop=True)
X_val_final[numericas] = X_val[numericas].reset_index(drop=True)

# Definir y ajustar el modelo de regresión logística
modeloRL = LogisticRegression(solver='liblinear', random_state=1)
modeloRL.fit(X_train_final, y_train)

# Obtener las probabilidades predichas
probs = modeloRL.predict_proba(X_val_final)
segunda_columna = probs[:, 1]

# Aplicar umbral de 0.5 para predicciones binarias
y_pred = (segunda_columna >= 0.5).astype(int)

# Calcular la exactitud del modelo
accuracy = accuracy_score(y_val, y_pred)

print(f"Exactitud del modelo: {accuracy:.2f}")
