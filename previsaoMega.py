import numpy as np
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.callbacks import EarlyStopping

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
    [27, 45, 49, 53, 55, 59],
   [4,32,39,48,51,57],
   [2,9,11,25,43,51],
   [20,27,41,47,53,54],
   [7,24,29,41,46,60],
   [4,12,32,45,49,58]

])

# Gerar dados de entrada (X) a partir da sequência fornecida
X_provided = np.array([
    y_provided[i:i+10].flatten() for i in range(len(y_provided) - 10)
])

# As saídas correspondentes serão o 11º e 12º conjuntos
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

# Configurar early stopping
early_stopping = EarlyStopping(monitor='loss', patience=5, restore_best_weights=True)

# Treinar o modelo com os dados fornecidos
model.fit(X_provided_normalized, y_target_normalized, epochs=100, batch_size=4, callbacks=[early_stopping])

# Função para normalizar e prever o próximo conjunto de números
def predict_next(input_sequence, model, scaler_X, scaler_y):
    input_normalized = scaler_X.transform(input_sequence)
    prediction_normalized = model.predict(input_normalized)
    prediction = scaler_y.inverse_transform(prediction_normalized)
    return prediction

# Previsões para o 13º ao 20º conjuntos de números
predictions = []
current_input = y_provided[-10:].flatten().reshape(1, -1)

for _ in range(8):  # Prever do 13º ao 20º
    next_prediction = predict_next(current_input, model, scaler_X, scaler_y)
    predictions.append(next_prediction[0])
    
    # Preparar a entrada para a próxima previsão
    current_input = np.append(current_input.flatten()[6:], next_prediction).reshape(1, -1)

# Exibir as previsões
for i, prediction in enumerate(predictions, start=13):
    print(f"Previsão para o {i}º conjunto de números:")
    print(prediction)
