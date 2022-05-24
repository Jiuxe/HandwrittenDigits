import pylab as pl
import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np

def trainingModel():

    # Obtenemos los datos de keras
    (x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

    # Normalizamos los resultados obtenidos para que esten entre 0 y 1,
    # en vez de 0 y 255
    x_train = x_train / 255
    x_test = x_test / 255

    # Convertimos las matrices en vectores
    x_train_flattened = x_train.reshape(len(x_train), 28*28) # El valor lo sabemos de hace x_train.shape()
    x_test_flattened = x_test.reshape(len(x_test), 28*28)

    # Creamos el modelo y lo entrenamos

    model.fit(x_train_flattened, y_train, epochs=5)

    # Evaluamos el modelo con los datos de Test
    model.evaluate(x_test_flattened, y_test)

def evaluateOneElement(image):

    # plt.matshow(image)
    # plt.waitforbuttonpress()

    image = image / 255

    image_flattened = image.reshape(1, 28 * 28)
    y_predict = model.predict(image_flattened)

    print(y_predict)

    return np.argmax(y_predict[0])


model = keras.Sequential([
    keras.layers.Dense(10, input_shape=(784,), activation='sigmoid')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

"""
# Probamos si el modelo se ha entrenado bien
y_predict = model.predict(x_test_flattened)


print(np.argmax(y_predict[0]))
plt.matshow(x_test[0])
plt.waitforbuttonpress()
"""
