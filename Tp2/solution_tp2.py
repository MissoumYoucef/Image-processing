# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 08:43:46 2023

@author: ait7m
"""

import numpy as np
from PIL import Image

a = np.array([[1,2], [3, 4]])
        
def ex01(a,n):
    e = np.zeros((a.shape[0] * n, a.shape[1] * n))
    
    for i in range(a.shape[0]): 
        for j in range(a.shape[1]):
            # e[2*i,2*j] = a[i, j] # e[0, 2] pour j = 1 avec a[0, 1] a la value 2
            # e[2*i,2*j + 1] = a[i, j] #  e[0, 3]
            # e[2*i + 1, 2*j] = a[i, j] #  e[1, 2]
            # e[2*i + 1, 2*j + 1] = a[i, j] #  e[1, 3]
            
            # e[2*i : 2*i + 2, 2*j : 2*j + 2] = a[i, j]
            e[n*i : n*i + n, n*j : n*j + n] = a[i, j]

    print(e)
    return e

def exo3():
    
    image= Image.open("B.jpg")
    
    image = np.array(image)
    Image.fromarray(image).show()
    nbligne,nbcolonne, _ = image.shape
    
    q1 = np.zeros((nbligne, nbcolonne,3), dtype = 'uint8')
    
    q2 = np.zeros((nbligne, nbcolonne,3), dtype = 'uint8')
    
    q3 = np.zeros((nbcolonne,nbligne,3), dtype = 'uint8')
    
    
    for i in range(nbligne ):
        for j in range(nbcolonne):
            q1[nbligne - i - 1, j] = image[i,j]
            q2[i, nbcolonne - j - 1] = image[i,j]
            q3[j, nbligne - i - 1] = image[i,j] # -i est (nbligne - i - 1)
            
    Image.fromarray(image).show()
    #Image.fromarray(q1).show() 
    Image.fromarray(q3).show() 


main(a, 2)
main(a, 8)


exo3()
# matA=np.array([[1,2],[3,4]])
# matA= np.insert(matA, 1, [1,3],axis=1)
# print("Matrice A= ",matA)
# matC= np.insert(matA, 3, [2,4],axis=1)
# print("Matrice C= ",matC)
# matE= np.insert(matC, 0, [1,1,2,2],axis=0)
# print("Matrice E0= ",matE)
# matE= np.insert(matE, 2, [3,3,4,4],axis=0)
# print("Matrice E1= ",matE)