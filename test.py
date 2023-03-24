
# from PIL import Image
# import numpy as np
# import cv2
# from keras.models import load_model
#
# # Загрузка обученной модели нейронной сети
# model = load_model('my_model.keras')
#
#
# def recognize():
#     file = r'image.jpg'
#     test_image = cv2.imread(file, cv2.IMREAD_GRAYSCALE)
#     img_resized = cv2.resize(test_image, (28, 28), interpolation=cv2.INTER_LINEAR)
#     img_resized = cv2.bitwise_not(img_resized)
#     cv2.imwrite(r'image_mnist.jpg', img_resized)
#
#     image = Image.open("image_mnist.jpg").convert('L')
#     image_array = np.array(image).reshape(1, 28, 28, 1) / 255.0
#     prediction = model.predict(image_array)
#     percent = prediction[0][np.argmax(prediction)]
#     percent = int(percent * 100)
#     digit = np.argmax(prediction)
#     print("Predicted digit:", digit)
#     print(percent)
#     return digit, percent
#
#
# recognize()
#
# if __name__ == '__main__':
#     pass