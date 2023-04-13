import tensorflow as tf
import cv2
import matplotlib.pyplot as plt

# Define the model
model = tf.keras.applications.MobileNetV2(input_shape=(224, 224, 3), include_top=False)

# Freeze the model layers
model.trainable = False

# Add a new layer for face detection
x = tf.keras.layers.GlobalAveragePooling2D()(model.output)
x = tf.keras.layers.Dense(128, activation='relu')(x)
x = tf.keras.layers.Dropout(0.2)(x)
outputs = tf.keras.layers.Dense(1, activation='sigmoid')(x)

# Create the new model
model = tf.keras.Model(inputs=model.input, outputs=outputs)

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Load the dataset
train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    'path/to/dataset',
    image_size=(224, 224),
    batch_size=32,
    validation_split=0.2,
    subset='training',
    seed=123
)

# Preprocess the images
train_dataset = train_dataset.map(lambda x, y: (tf.image.resize(x, (224, 224)), y))

# Train the model
history = model.fit(
    train_dataset,
    epochs=10,
    validation_data=val_dataset
)

# Load a test image
img = cv2.imread('path/to/image.jpg')

# Preprocess the image
img = cv2.resize(img, (224, 224))
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img = img / 255.0

# Predict if the image contains a face
prediction = model.predict(np.expand_dims(img, axis=0))[0][0]

# Display the image and prediction
plt.imshow(img)
if prediction > 0.5:
    plt.title('Face Detected')
else:
    plt.title('No Face Detected')
plt.show()

