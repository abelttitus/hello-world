# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 08:46:56 2019

@author: student
"""

import tensorflow as tf
from tensorflow import keras
from keras.utils import plot_model

import numpy as np
import matplotlib.pyplot as plt

fashion_mnist=keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat', 
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#plt.figure(figsize=(10,10))
#for i in range(1,26):
#    plt.subplot(5,5,i)
#    plt.xticks([])
#    plt.yticks([])
#    plt.imshow(train_images[i],cmap=plt.cm.binary)
#    plt.xlabel(class_names[train_labels[i]])
#    plt.show()

model=keras.Sequential([
        keras.layers.Flatten(input_shape=(28,28)),
        keras.layers.Dense(128,activation=tf.nn.softmax),
        keras.layers.Dense(10,activation=tf.nn.relu)
        ])
    
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images,train_labels,epochs=5)
test_loss,test_acc=model.evaluate(test_images,test_labels)
print('Test Accuracy',test_acc)


#plot_model(model)