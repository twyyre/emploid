import tensorflow as tf
import numpy as np

# Define the model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Dense(64, activation='relu', input_shape=(10,)),
    tf.keras.layers.Dense(64, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile the model
model.compile(
    optimizer='adam',
    loss='binary_crossentropy',
    metrics=['accuracy']
)

# Generate some random training data
train_data = np.random.rand(1000, 10)
train_labels = np.random.randint(2, size=(1000, 1))

# Train the model
model.fit(train_data, train_labels, epochs=10, batch_size=32)

# Generate some random test data
test_data = np.random.rand(100, 10)
test_labels = np.random.randint(2, size=(100, 1))

# Evaluate the model on the test data
test_loss, test_acc = model.evaluate(test_data, test_labels)

print('Test accuracy:', test_acc)