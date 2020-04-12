# -*- coding: utf-8 -*-
"""MLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dSjXQQr3Q87NEUSTgVe8tdFp8OSPQM4N
"""

from warnings import filterwarnings
filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import fetch_openml
import matplotlib.pyplot as plt
import numpy as np
import random

X, y = fetch_openml('mnist_784', return_X_y=True)
X /= 255
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

mlp = MLPClassifier(hidden_layer_sizes=(30), max_iter=10, alpha=0.001, solver='sgd', verbose=True, learning_rate_init=0.01)

mlp.fit(X_train, y_train)
print("Training Accuracy: ", mlp.score(X_train, y_train))

mlp.fit(X_test, y_test)
print("Testing Accuracy: ", mlp.score(X_test, y_test))

fig, ax = plt.subplots(nrows=3, ncols=3, figsize=(8, 8))
for i, axis in enumerate(ax.flat):
  sample = np.expand_dims(X_test[random.randint(0, X_test.shape[0] - 1)], 0)
  predicted_cls = mlp.predict(sample)
  digit_img = sample.reshape((28, 28)) * 255
  axis.imshow(digit_img)
  axis.set_title('Prediction: {}'.format(predicted_cls[0]))
  axis.set_xticks([])
  axis.set_yticks([])

plt.show()