# Supongamos que X y y son el dataset completo (sin la división en train/test)
# Si ya tienes X_train e y_train, y deseas reentrenar el modelo final en todos ellos:
best_knn.fit(X_train, y_train)

# O, si deseas usar todos los datos (train + test), combínalos:
X_total = pd.concat([X_train, X_test])
y_total = pd.concat([y_train, y_test])

# Reentrena el modelo final en todo el dataset
best_knn.fit(X_total, y_total)
