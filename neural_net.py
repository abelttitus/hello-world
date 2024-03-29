#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 30 22:24:11 2019

@author: abel
"""
import numpy as np

class Network(object):
    def __init__(self,sizes):
        self.num_layers=len(sizes)
        self.sizes= sizes
        self.biases=[np.random.randn(y,1) for y in sizes[1:]] 
        self.weights=[np.random.randn(y,x) for x,y in zip(sizes[:-1],sizes[1:]) ]
        
#    def feedfoward(self,a):
        
def sigmoid(z):
    return 1/(1+np.exp(-z))

net=Network([2,2])

for b,w in zip(net.biases,net.weights):
    print("bias",b,"wei",w)
