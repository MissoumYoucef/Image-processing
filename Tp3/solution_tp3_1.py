# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 08:30:58 2023

@author: ait7m
"""


import numpy as np
from PIL import Image

import numpy as np 
from PIL import Image
import matplotlib.pyplot as plt
import scipy.ndimage


#K--> modifier le contraste, 
#k>1 is used to increase the contrast
#0<k<1 is used to decrease the contrast
#k=1 is adjust the brightness of the image
# k=-1 et d=255, on obtient alors l'inverse de l'image


# #d --> modifier l'illumination

def niveaux_gris(image, k, d):
    
    image = np.array(image)
    
    image = np.array(k*image + d, dtype='uint8')
    
    q1 = np.zeros((image.shape[0], image.shape[1]))
    
    for i in range(image.shape[0]):
        
        for j in range(image.shape[1]):
            
            q1[i, j] = k * image[i,j] + d
            
    image = np.array(q1, dtype='uint8')
    
    return Image.fromarray(image)


def 𝐼𝑚𝑔𝐼𝑛𝑣𝑒𝑟𝑠𝑒(image):
    
    image = np.array(image)
    
    return Image.fromarray(255  - image)


def t_logarithmique(image):
    
    image = np.array(image)
   
    
    C = 255 / np.log(np.max(image)) # remettre l'intervalle de variation de c entre 0 et 255
    
    image = C * np.log(1 + image) # + 1 pour éviter le cas de log(0)
    
    image = np.array(image, dtype='uint8')
    
    return Image.fromarray(image)


def correctiongamma(image, gamma, c = 255):
    
    image = np.array(image)
    # normaliser image sur 255 pour avoir l'intervalle [0,1]
    # multiplier par 255 pour intensités entre [0 255] 
    image = image / c
    image = np.power(image, gamma)
    image = c * image

    image = np.array(image, dtype='uint8')

    return Image.fromarray(image)


def ajustementcontraste(l,kmin = 0, kmax = 255):    

    ll = kmin + ((kmax - kmin) / (lmax - lmin)) * (l - lmin)
    
    return ll


image= Image.open("C.jpg")
print(image.size)
image.show()

r_intensity, g_intensity, b_intensity = image.split()


img = Image.merge("RGB", (r_intensity, g_intensity, b_intensity))

fig,(ax1,ax2,ax3) = plt.subplots(1, 3,figsize=(24,6))

ax1.set_xlabel("red value")
ax1.set_ylabel("Pixel count")
ax1.set_xlim([0, 255])
ax1.hist(np.array(r_intensity).ravel(), 256, [0,255], color = 'red')

ax2.set_xlabel("Green value")
ax2.set_ylabel("Pixel count")
ax2.set_xlim([0, 255])
ax2.hist(np.array(g_intensity).ravel(), 256, [0,255], color = 'green')

ax3.set_xlabel("Blue value")
ax3.set_ylabel("Pixel count")
ax3.set_xlim([0, 255])
ax3.hist(np.array(b_intensity).ravel(), 256, [0,255], color = 'blue')

#plt.show()
# fig.savefig("histogram1.png")




lmin,lmax = None, None

lmin,lmax = np.min(np.array(r_intensity)), np.max(np.array(r_intensity))
print("lmin,lmax r : ",lmin,lmax)
r_intensity = r_intensity.point(ajustementcontraste) # la fonction point elle applique la fonction ajustementcontraste pour chaque pixl

lmin,lmax = np.min(np.array(g_intensity)), np.max(np.array(g_intensity))
print("lmin,lmax g : ",lmin,lmax)

g_intensity = g_intensity.point(ajustementcontraste)

lmin,lmax = np.min(np.array(b_intensity)), np.max(np.array(b_intensity))
print("lmin,lmax b : ",lmin,lmax)

b_intensity = b_intensity.point(ajustementcontraste)



img = Image.merge("RGB", (r_intensity, g_intensity, b_intensity))

fig,(ax1,ax2,ax3) = plt.subplots(1, 3,figsize=(24,6))

ax1.set_xlabel("red value")
ax1.set_ylabel("Pixel count")
ax1.set_xlim([0, 255])
ax1.hist(np.array(r_intensity).ravel(), 256, [0,255], color = 'red')

ax2.set_xlabel("Green value")
ax2.set_ylabel("Pixel count")
ax2.set_xlim([0, 255])
ax2.hist(np.array(g_intensity).ravel(), 256, [0,255], color = 'green')

ax3.set_xlabel("Blue value")
ax3.set_ylabel("Pixel count")
ax3.set_xlim([0, 255])
ax3.hist(np.array(b_intensity).ravel(), 256, [0,255], color = 'blue')

plt.show()
fig.savefig("histogram2.png")

Image.open("histogram2.png").show()


    
