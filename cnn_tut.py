# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 10:03:10 2019

@author: student
"""

import numpy as np
import pickle
import matplotlib.pyplot as plt
from keras.datasets import cifar10

#file_loc='';
#file=open(file_loc,'rb')
#data=pickle.load(file)
#data=np.reshape(data,(10000,3,32,32))
#data=np.transpose(data,(0,2,3,1))

(x_train,y_train),(x_test,y_test)=cifar10.load_data()

def load_class_names(index):
    class_name=['airplane','automobile','bird','cat','deer','dog','frog','horse','ship','truck']
    return class_name[index]

def normalize(x):
    maxi=np.max(x)
    mini=np.min(x)
    x=(x-mini)/(maxi-mini)
    return x

def one_hot_encode(x):
    encoded=np.random.rand(len(x),10)
    for i in range(len(x)):
        encoded[i]=np.zeros((10))
        encoded[i][x[i]]=1
    return encoded

x_train=normalize(x_train)
y_train_vector=one_hot_encode(y_train)
