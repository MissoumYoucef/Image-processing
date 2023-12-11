# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 08:41:28 2023

@author: ait mehdi
"""

from PIL import Image
import  numpy as np

def exo1(): 

    try: 
        img=Image.open('A.jpg') 
        print(img.width, img.height, img.mode, img.format, type(img))
        img = img.convert('L')
        img = np.array(img)
        print("img.shape = ",img.shape)
        print("pixel de coordonnée (400,250) : ",img[400,  255])
        img[:400,  100:255] = [60]
        Image.fromarray(img).show()
    except IOError: 
        print('image not found !')


def exo3():
    
    try: 
        img=Image.open('A.jpg') 
        img = np.array(img)
        print("img.shape = ",img.shape)

        # 4) Convert image B (RGB) to grayscale
        l = []
        for row in img:
            ligne = []
            for pix in row:
                ligne.append(sum(pix)/3) # row est un tableau de 3 valeur (R,G, B)
            l.append(ligne)
        #or 
        l1 = [[(sum(pix) / 3) for pix in row] for row in img ]
        
        # 5) Extract the red, green, and blue channels from image D

        red, blue, green = [], [], []
        for row in img:
            row_red, row_blue, row_green = [], [], []
            for pix in row :
                row_red.append([pix[0], 0, 0])
                row_green.append([0, pix[1], 0])
                row_blue.append([0, 0, pix[2]])
                
            red.append(row_red)
            blue.append(row_blue)
            green.append(row_green)
        
        blue = np.array(blue, dtype=np.uint8)
        Image.fromarray(blue).show()
        # or 
        red = [  [[pix[0], 0, 0] for pix in row]  for row in img] # pour chaque row in img, nous avons un tableau [[pix[0], 0, 0] for pix in row]
        red = np.array(red, dtype=np.uint8)
        Image.fromarray(red).show()
        
        # essayer de faire la question 6, le négatif de l’image D.
        
    except IOError: 
        print('image not found !')
    

if __name__ == "__main__": 
    exo1()
