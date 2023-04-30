import os

from keras import Sequential
from keras.layers import Dropout

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'  # Блокировка сообщения о использовании процессора

from tensorflow.keras.datasets import mnist
from tensorflow import keras
from tensorflow.keras.layers import Dense, Flatten, Conv2D, MaxPooling2D
import matplotlib.pyplot as plt

(x_train, y_train), (
x_test, y_test) = mnist.load_data()  # Выгружаем данные из mnist (x - входные данные y - ожидаемый результат)

# Нормализуем тестовые и обучающие данные
x_train = x_train / 255
x_test = x_test / 255

y_train = keras.utils.to_categorical(y_train, 10)
y_test = keras.utils.to_categorical(y_test, 10)

model = Sequential([  # Сверточная архитектура нейросети
    Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    MaxPooling2D((2, 2)),
    Conv2D(64, (3, 3), activation='relu'),
    MaxPooling2D((2, 2)),
    Flatten(),
    Dense(128, activation='relu'),
    Dense(10, activation='softmax')
])

# model = keras.Sequential([ # Полносвязная архитектура нейросети
#     Flatten(input_shape=(28, 28, 1)),
#     Dense(300, activation='relu'),
#     Dense(100, activation='relu'),
#     Dense(10, activation='softmax')
# ])

# Большая сверточная сеть
# num_classes = y_test.shape[1]
# model = Sequential()
# model.add(Conv2D(30, (5, 5), input_shape=(28, 28, 1), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Conv2D(15, (3, 3), activation='relu'))
# model.add(MaxPooling2D(pool_size=(2, 2)))
# model.add(Dropout(0.2))
# model.add(Flatten())
# model.add(Dense(128, activation='relu'))
# model.add(Dense(50, activation='relu'))
# model.add(Dense(num_classes, activation='softmax'))

# from sklearn.model_selection import train_test_split

# x_train_split, x_test_split, y_train_split, y_test_split = train_test_split(x_train, y_train, test_size=0.2)

# Определение метрик, функции ошибки и оптимизации для обучения
model.compile(optimizer="adam", loss='categorical_crossentropy', metrics=['accuracy'])

# his = model.fit(x_train_split, y_train_split, batch_size=32, epochs=5, validation_data=(x_test_split, y_test_split))
# his = model.fit(x_train, y_train, batch_size=32, epochs=10, validation_split=0.2) # Для небольшой сверточной модели


# Запуск обучения сети, установка кол-ва эпох и батча
# (эпоха - кол-ва итераций прогона обучающих данных, батч - часть данных использующаяся в эпохе)
his = model.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=10,
                batch_size=200)  # Для большой сверточной модели
model.evaluate(x_test, y_test)

# График отображающий процесс обучения
plt.plot(his.history['loss'])
plt.plot(his.history['val_loss'])
plt.show()

# Сохранения модели в файл
model.save('my_model_complex_cnn.keras')
