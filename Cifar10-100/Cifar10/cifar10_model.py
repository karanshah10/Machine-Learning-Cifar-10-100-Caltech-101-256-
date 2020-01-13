# -*- coding: utf-8 -*-
"""cifar10_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QZc8rKud-pbsFBVhsC2AjvmEE-hf4gfY
"""

from keras.models import Sequential
from keras.layers import GlobalAveragePooling2D,Conv2D, Dropout, Activation

def cifar10_model():
    model = Sequential()
    
    model.add(Conv2D(96, (3, 3), padding = 'same', input_shape=(32,32,3)))    
    model.add(Activation('relu'))
    model.add(Dropout(0.2))
    
    model.add(Conv2D(96, (3, 3), padding = 'same'))  
    model.add(Activation('relu'))
    model.add(Conv2D(96, (3, 3), padding = 'same', strides = 2))    
    model.add(Activation('relu'))
    model.add(Dropout(0.5))
    
    model.add(Conv2D(192, (3, 3), padding = 'same'))   
    model.add(Activation('relu')) 
    model.add(Conv2D(192, (3, 3), padding = 'same'))
    model.add(Activation('relu'))
    model.add(Conv2D(192, (3, 3), padding = 'same', strides = 2))   
    model.add(Activation('relu')) 
    model.add(Dropout(0.5))    
    
    model.add(Conv2D(192, (3, 3), padding = 'same'))
    model.add(Activation('relu'))
    model.add(Conv2D(192, (1, 1),padding='valid'))
    model.add(Activation('relu'))
    model.add(Conv2D(10, (1, 1), padding='valid'))

    model.add(GlobalAveragePooling2D())
    model.add(Activation('softmax'))
    return model