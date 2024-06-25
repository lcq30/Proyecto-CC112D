import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
# Crear y ajustar el modelo de regresión
modeloRL = LogisticRegression(solver='liblinear', random_state=1)
modeloRL.fit(X_train, y_train)
val_dict = df_val[categoricas + numericas].to_dict(orient='records')
X_val = dv.transform(val_dict)
probs = modeloRL.predict_proba(X_val)
# Obtener solo la segunda columna de las probabilidades predichas
segunda_columna = probs[:, 1]
print(segunda_columna)
