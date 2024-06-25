import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_recall_curve, auc
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.feature_extraction import DictVectorizer
def entrenamiento(df, y, C=1.0):
    cat = df[categoricas + numericas].to_dict(orient='records')
    dv = DictVectorizer(sparse=False)
    dv.fit(cat)

    X = dv.transform(cat)

    modelRL = LogisticRegression(solver='liblinear', C=C)
    modelRL.fit(X, y)

    return dv, modelRL
def predict(df, dv, modelo, umbral=0.5):
    cat = df[categoricas + numericas].to_dict(orient='records')
    X = dv.transform(cat)
    y_pred_proba = modelo.predict_proba(X)[:, 1]
    y_pred = (y_pred_proba >= umbral).astype(int)
    return y_pred
nfolds = 5
kfold = KFold(n_splits=nfolds, shuffle=True, random_state=1)
valores_C = [0.001, 0.01, 0.1, 0.5, 1, 10]
precisiones_medias = []
exhaustividades_medias = []
for C in valores_C:
    precisiones = []
    exhaustividades = []

    # Validación cruzada
    for train_idx, val_idx in kfold.split(df_train_completo):
        df_train = df_train_completo.iloc[train_idx]
        df_val = df_train_completo.iloc[val_idx]

        y_train = df_train.churn.values
        y_val = df_val.churn.values

        dv, modelo = entrenamiento(df_train, y_train, C=C)
        y_pred_proba = modelo.predict_proba(dv.transform(df_val[categoricas + numericas].to_dict(orient='records')))[:, 1]
        precision, exhaustividad, _ = precision_recall_curve(y_val, y_pred_proba)
        precisiones.append(precision)
        exhaustividades.append(exhaustividad)
    precision_media = np.mean(precisiones, axis=0)
    exhaustividad_media = np.mean(exhaustividades, axis=0)

    precisiones_medias.append(precision_media)
    exhaustividades_medias.append(exhaustividad_media)
    f1_scores = 2 * (precision_media * exhaustividad_media) / (precision_media + exhaustividad_media + 1e-10)
    umbral_optimo = np.argmax(f1_scores)
    plt.figure(figsize=(8, 6))
    plt.plot(exhaustividad_media, precision_media, label=f'C={C}')
    plt.scatter(exhaustividad_media[umbral_optimo], precision_media[umbral_optimo], marker='o', color='r', label=f'Umbral óptimo = {exhaustividad_media[umbral_optimo]:.2f}')

    plt.xlabel('Exhaustividad')
    plt.ylabel('Precisión')
    plt.title(f'Curva de Precisión-Exhaustividad para C={C}')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    print(f'Umbral óptimo seleccionado para C={C}: {exhaustividad_media[umbral_optimo]:.3f}')

mejor_C = 0.5
dv, modelo = entrenamiento(df_train_completo, y_train, C=mejor_C)
y_pred_proba_test = modelo.predict_proba(dv.transform(df_test[categoricas + numericas].to_dict(orient='records')))[:, 1]

precision_test, exhaustividad_test, _ = precision_recall_curve(y_test, y_pred_proba_test)
area_bajo_curva = auc(exhaustividad_test, precision_test)

print(f'AUC de Precisión-Exhaustividad en el conjunto de prueba: {area_bajo_curva:.3f}')
