import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_diabetes #para asignar variables
from sklearn.model_selection import train_test_split #para dividir y probar el conjunto de datos
from sklearn.linear_model import LinearRegression, Ridge, Lasso #para usar las regresiones
from sklearn.preprocessing import StandardScaler

# Cargar el conjunto de datos
diabetes = load_diabetes()
X = diabetes.data
y = diabetes.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Inicializar los modelos
linear_reg = LinearRegression()
#crea un objeto de regresión con regularizacion
ridge_reg = Ridge(alpha=1.0)  # Usaremos alpha=1.0 por defecto
lasso_reg = Lasso(alpha=0.1)  # Usaremos alpha=0.1 por defecto

# Ajustar los modelos
linear_reg.fit(X_train, y_train)
ridge_reg.fit(X_train, y_train)
lasso_reg.fit(X_train, y_train)

coefficients = {
    'Linear Regression': linear_reg.coef_,
    'Ridge': ridge_reg.coef_,
    'Lasso': lasso_reg.coef_
}

# Visualizar los coeficientes
plt.figure(figsize=(10, 6))
plt.barh(range(len(linear_reg.coef_)), linear_reg.coef_, color='b', align='center', label='Linear Regression')
plt.barh(range(len(ridge_reg.coef_)), ridge_reg.coef_, color='g', align='center', label='Ridge')
plt.barh(range(len(lasso_reg.coef_)), lasso_reg.coef_, color='r', align='center', label='Lasso')
plt.yticks(range(len(diabetes.feature_names)), diabetes.feature_names)
plt.xlabel('Coefficient Value')
plt.ylabel('Feature')
plt.title('Comparison of Coefficients')
plt.legend()
plt.tight_layout()
plt.show()
