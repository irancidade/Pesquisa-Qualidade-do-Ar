import numpy as np
import tensorflow as tf

# Gerar dados de treinamento
def generate_data(n_samples=1000):
    X = np.random.randint(1, 61, size=(n_samples, 10))  # Conjunto de 10 números
    y = np.array([sorted(np.random.choice(range(1, 61), size=6, replace=False)) for _ in range(n_samples)])  # Padrão de 6 números
    return X, y

X_train, y_train = generate_data()

# Normalização dos dados
X_train_normalized = X_train / 60.0
y_train_normalized = y_train / 60.0

# Construir a rede neural
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(128, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(32, activation='relu'),
    tf.keras.layers.Dense(6, activation='sigmoid')  # Seis saídas para os seis números
])

# Compilar o modelo
model.compile(optimizer='adam', loss='mean_squared_error')

# Treinar o modelo
model.fit(X_train_normalized, y_train_normalized, epochs=60, batch_size=32)

# Testar o modelo
X_test, y_test = generate_data(100)
X_test_normalized = X_test / 60.0
y_test_normalized = y_test / 60.0

predictions = model.predict(X_test_normalized)

# Desnormalizar as previsões
predictions = predictions * 60.0

print("Previsões:")
print(predictions)
print("\nValores reais:")
print(y_test)
