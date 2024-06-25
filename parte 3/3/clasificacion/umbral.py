import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
modeloRL = LogisticRegression(solver='liblinear', random_state=1)
modeloRL.fit(X_train, y_train)
val_dict = df_val[categoricas + numericas].to_dict(orient='records')
X_val = dv.transform(val_dict)
probs = modeloRL.predict_proba(X_val)
predicciones_binarias = (probs[:, 1] >= 0.5).astype(int)
exactitud = accuracy_score(y_val, predicciones_binarias)

print(f'Exactitud del modelo: {exactitud:.4f}')
