import numpy as np
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error # para calcular el error cuadratico medio

diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target
#elimina las columnas de índice 0 y 8 de la matriz
X_filtered = np.delete(X, [0, 8], axis=1)
X_train, X_test, y_train, y_test = train_test_split(X_filtered, y, test_size=0.2, random_state=1)
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
#calcular el error cuadratico medio
mse = mean_squared_error(y_test, y_pred)

print(f"Mean Squared Error (MSE) con características menos útiles eliminadas: {mse:.2f}")
'''
La característica “contract” probablemente contiene información crucial 
sobre el tipo de contrato del paciente. Esto puede estar directamente relacionado 
con su nivel de atención médica y, por lo tanto, afectar la respuesta a tratamientos 
y la evolución de la enfermedad. Al eliminar esta característica, 
el modelo podría perder parte de su capacidad para capturar estas variaciones,
 lo que podría resultar en una reducción en la precisión de las predicciones.
'''