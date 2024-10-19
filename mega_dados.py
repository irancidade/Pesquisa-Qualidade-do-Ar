import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

# Sequência fornecida de 12 conjuntos de 6 números
y_provided = np.array([
    [7, 19, 25, 46, 50, 53],
    [5, 20, 27, 28, 48, 49],
    [6, 22, 34, 36, 44, 50],
    [6, 30, 34, 41, 46, 59],
    [11, 25, 27, 30, 42, 48],
    [8, 15, 16, 23, 42, 43],
    [9, 10, 11, 25, 36, 46],
    [19, 23, 25, 36, 44, 46],
    [6, 12, 19, 28, 50, 60],
    [11, 21, 24, 26, 42, 54],
    [2, 10, 32, 33, 38, 47],
    [21, 45, 49, 53, 55, 59]
])

# Gerar dados de entrada (X) a partir da sequência fornecida
# Usaremos os primeiros 11 conjuntos como entrada para prever o 12º, e assim por diante
X_provided = np.array([
    y_provided[i:i+10].flatten() for i in range(len(y_provided) - 2)
])

# As saídas correspondentes serão os 12º e 13º conjuntos
y_target = y_provided[10:]

# Normalização dos dados
scaler_X = MinMaxScaler()
scaler_y = MinMaxScaler()

X_provided_normalized = scaler_X.fit_transform(X_provided)
y_target_normalized = scaler_y.fit_transform(y_target)

# Construir a rede neural
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(60,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(6, activation='sigmoid')  # Seis saídas para os seis números
])

# Compilar o modelo
model.compile(optimizer='adam', loss='mean_absolute_error')

# Treinar o modelo com os dados fornecidos
model.fit(X_provided_normalized, y_target_normalized, epochs=50, batch_size=4)

# Prever o próximo resultado (13º)
next_input = y_provided[-10:].flatten().reshape(1, -1)
next_input_normalized = scaler_X.transform(next_input)
next_prediction_normalized = model.predict(next_input_normalized)
next_prediction = scaler_y.inverse_transform(next_prediction_normalized)

print("Previsão para o 13º conjunto de números:")
print(next_prediction[0])

# Para prever o 14º, utilizamos os últimos 10 conjuntos incluindo a previsão do 13º
new_input = np.append(y_provided[-9:].flatten(), next_prediction).reshape(1, -1)
new_input_normalized = scaler_X.transform(new_input)
new_prediction_normalized = model.predict(new_input_normalized)
new_prediction = scaler_y.inverse_transform(new_prediction_normalized)

print("Previsão para o 14º conjunto de números:")
print(new_prediction[0])
