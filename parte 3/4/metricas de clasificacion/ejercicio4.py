import numpy as np
import matplotlib.pyplot as plt

def entrenamiento(df, y, C=1.0):
    cat = df[categoricas + numericas].to_dict(orient='records')
    dv = DictVectorizer(sparse=False)
    dv.fit(cat)

    X = dv.transform(cat)

    modelRL = LogisticRegression(solver='liblinear', C=C)
    modelRL.fit(X, y)

    return dv, modelRL

nfolds = 10
nrepeats = 10
rkf = RepeatedKFold(n_splits=nfolds, n_repeats=nrepeats, random_state=1)
valores_C = [0.001, 0.01, 0.1, 0.5, 1, 10]
auc_scores = []
for C in valores_C:
    auc_scores_C = []
    for train_idx, val_idx in rkf.split(df_train_completo):
        df_train = df_train_completo.iloc[train_idx]
        df_val = df_train_completo.iloc[val_idx]

        y_train = df_train.churn.values
        y_val = df_val.churn.values

        dv, modelo = entrenamiento(df_train, y_train, C=C)
        y_pred_proba = modelo.predict_proba(dv.transform(df_val[categoricas + numericas].to_dict(orient='records')))[:, 1]

        auc = roc_auc_score(y_val, y_pred_proba)
        auc_scores_C.append(auc)
    auc_scores.append(auc_scores_C)
auc_scores = np.array(auc_scores)
plt.figure(figsize=(10, 6))
plt.boxplot(auc_scores.T, labels=valores_C)
plt.xlabel('Valor de C')
plt.ylabel('Puntuación AUC')
plt.title(f'Distribución de las puntuaciones AUC con {nfolds}-fold {nrepeats}-repeats CV')
plt.grid(True)
plt.tight_layout()
plt.show()
