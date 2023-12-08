
import numpy as np
from PIL import Image



def dilate_Nenni(image, kernel):
    result = np.zeros([image.shape[0],image.shape[1]])
    image_padded = np.pad(image, ((1, 1), (1, 1)), mode='constant', constant_values=0)

    for i in range(1, image.shape[0] + 1):
        for j in range(1, image.shape[1] + 1):
            if np.sum(kernel * image_padded[i - 1:i + 2, j - 1:j + 2]) > 0:
                result[i - 1, j - 1] = 1
                
    return result * 255

def img_binaire(img):

    new_img = [ [255 if pix >=128 else 0 for pix in row] for row in img    ]


    img[img >= 128] = 255 # 255
    img[img < 128] = 0

    print(img)


    new_img = np.array(new_img, dtype=np.uint8)

    


    return img



def dialte(img, e):
    
    # matrix of zeros
    new = np.zeros((img.shape[0], img.shape[1]), dtype=np.uint8)
    
    for i in range(e.shape[0]):
        for j in range(e.shape[1]):
            
            if e[i, j] == 1:
                
                for u in range(img.shape[0] - e.shape[0]):
                    for v in range(img.shape[1] - e.shape[1]):
                        if img[u,v] == 255:
                            new[u + i , v + j] = 255
                        
                            
    return new 


def reflexion(e):
    
    e_ref = np.zeros((e.shape[0], e.shape[1]))
    
    
    for i in range(e.shape[0]):
        
        for j in range(e.shape[1]):
            
            e_ref[e.shape[0]  - i - 1, e.shape[1]  - j - 1] = e[i,j]
    
    
    return e_ref

def Erosion(img , e):
    
    img =  255 - img 
    
    e = reflexion(e) # e*
    
    return 255 - dialte(img, e)

# Show image
img_url="TP5\TP5\A22.jpg"
img=Image.open(img_url)
# img.show()

# Convert image to grayscale
img_grey=img.convert('L')

# Convert image to matrix
img_matrix = np.array(img_grey)

# Convert image to binary
img_binaire = img_binaire(img_matrix)
# Image.fromarray(img_binaire).show()

# e1, e2
e1 = np.ones((3,3))
e2 = np.array([[0,1,0], [1,1,1], [0,1,0]])

# dialting of the image
img_dialted = dialte(img_binaire, e1)
# Image.fromarray(img_dialted).show()



# reflexion de e2
print("reflexion de e2 : ",reflexion(e2))



# print("e1, img : ", e1.shape, img.shape)
# print("reflexion de e2 : ",reflexion(e2))


# img1 = dialte(img, e1)
# Image.fromarray(img1).show()

# img = np.array(Image.open("A.jpg").convert('L'))
# img = img_binaire(img)
# img1 = dialte(img, e1)
# img2 = Erosion(img, e1)

# Image.fromarray((img1 - img2)).show()



