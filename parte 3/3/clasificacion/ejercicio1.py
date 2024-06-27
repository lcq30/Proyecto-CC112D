import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.metrics import mean_squared_error

# Cargar el conjunto de datos de diabetes
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target
#divido en un 80% para entrenamiento y 20% para prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
#inicializo los modelos de regresion
linear_reg = LinearRegression()
ridge_reg = Ridge(alpha=0.1)  # Alpha es el parámetro de regularización
lasso_reg = Lasso(alpha=0.1)
#ajustar
linear_reg.fit(X_train, y_train)
ridge_reg.fit(X_train, y_train)
lasso_reg.fit(X_train, y_train)
#calculo el coeficiente de determinación R2 de cada dato de prueba
linear_reg_score = linear_reg.score(X_test, y_test)
ridge_reg_score = ridge_reg.score(X_test, y_test)
lasso_reg_score = lasso_reg.score(X_test, y_test)
print(f"R2 score de regresión lineal: {linear_reg_score:.2f}")
print(f"R2 score de Ridge regression: {ridge_reg_score:.2f}")
print(f"R2 score de Lasso regression: {lasso_reg_score:.2f}")
#creo un grafico
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(linear_reg.coef_, color='b', linestyle='-', linewidth=1, label='Regresión Lineal')
ax.plot(ridge_reg.coef_, color='r', linestyle='--', linewidth=1, label='Ridge')
ax.plot(lasso_reg.coef_, color='g', linestyle=':', linewidth=1, label='Lasso')

ax.set_xlabel('Coeficientes')
ax.set_ylabel('Valor')
ax.set_title('Coeficientes de los modelos de regresión')
ax.legend()

plt.tight_layout()
plt.show()

