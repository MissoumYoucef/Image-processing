# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 08:19:22 2023

@author: ait7m
"""

import numpy as np
import matplotlib as plt
from PIL import Image


def histogramme_normalis(image):
    hist, _ = np.histogram(image.ravel(), bins = 256, range=[0,255])
    
    pi = hist / image.size # nombre de pixel
    
    return pi

def formule_p1(pi,k):
    
    p1 = np.sum(pi[:k]) # de 0 à k 
    #  or 
    p1 = 0
    for i in range(0, k):
        p1+=pi[i]  # p1 = p1 + pi[i]
    
    
    return p1

def formule_p2(pi,k):
    
    p2 = np.sum(pi[k:])
    #  or 
    p2 = 0
    for i in range(k, 256): # de k à 255
        p2 += pi[i] # p2 = p2 + pi[i]
    
    
    return p2

def formule_m1(pi, k):
    
    p1 = formule_p1(pi, k)
    
    if p1 <=0:
         return 0
     
    m1 = 0
    
    for i in range(0, k):
        
        m1+= i * pi[i]
    
    m1 = m1 / p1
    
    return m1

def formule_m2(pi, k):
    
    p2 = formule_p2(pi, k)
    
    if p2 <=0:
        return 0
    
    m2 = 0
    
    for i in range(k, 256):
        
        m2+= i * pi[i]
    
    m2 = m2 / p2
    
    return m2

def Otsu(image):
    
    pi = histogramme_normalis(image)
    
    #print(pi.shape) # 256 c'est le nombre max de niveau de gris 
    
    p1,p2,m1,m2 = np.zeros(256), np.zeros(256), np.zeros(256), np.zeros(256)
    mg, var = np.zeros(256), np.zeros(256)
    
    for k in range(0, 256):
        
        p1[k] = formule_p1(pi, k)
        p2[k] = formule_p2(pi, k)

        m1[k] = formule_m1(pi, k)
        m2[k] = formule_m2(pi, k)
        
        mg[k] = p1[k] * m1[k] + p2[k] * m2[k]
        
        var[k] = p1[k] * (m1[k] - mg[k]) ** 2 + p2[k] * (m2[k] - mg[k]) ** 2 
        
    print("le seuil k maximisant var est :", np.argmax(var), np.max(var), var[np.argmax(var)])
    
    k = np.argmax(var)
    
    return k
    

def seuillage(image,k):
    
    image[image < k ] = 0
    image[image >= k ] = 255
    
    return np.array(image, dtype='uint8')

img_a = Image.open("./A.jpg").convert('L')


img_a = np.array(img_a)

k = Otsu(img_a)

img_a = seuillage(img_a, k )

Image.fromarray(img_a).show()

# img_b = Image.open("./B.jpg")

# img_r, img_g, img_bl = img_b.split()


# k_r = Otsu(img_r)

