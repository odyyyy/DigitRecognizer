import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Блокировка сообщения о использовании процессора

from tensorflow.keras.datasets import mnist
from tensorflow import keras
import matplotlib.pyplot as plt
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D

(x_train, y_train), (x_test, y_test) = mnist.load_data()

x_train = x_train / 255
x_test = x_test / 255

y_train_cat = keras.utils.to_categorical(y_train, 10)
y_test_cat = keras.utils.to_categorical(y_test, 10)

# model = keras.Sequential([
#     Flatten(input_shape=(28, 28, 1)),
#     Dense(512, activation='relu'),
#     Dense(10, activation='softmax')
# ])
model = keras.Sequential([
    Flatten(input_shape=(28, 28, 1)),
    Dense(300, activation='relu'),
    Dense(100, activation='relu'),
    Dense(10, activation='softmax')
])

# model = keras.Sequential()
# model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(28, 28, 1)))
# model.add(Conv2D(64, (3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Flatten())
# model.add(Dense(128, activation='relu'))
# model.add(Dense(10, activation='softmax'))

model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])

# model.fit(x_train, y_train_cat, batch_size=32, epochs=5, validation_split=0.2)
# model.fit(x_train, y_train_cat, epochs=10, batch_size=128)
model.fit(x_train, y_train_cat, epochs=30)
model.evaluate(x_test, y_test_cat)

model.save('my_model.keras')