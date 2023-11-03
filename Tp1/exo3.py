# Exercice 3 :
# Téléchargez les images suivantes : B.jpg, C.jpg, D.jpg.
# En utilisant le langage de programmation Python, écrire un script python qui permet de :
# 1) Accéder à un pixel donné dans l’image B,
# 2) Modifier un pixel donné dans l’image B,
# 3) Calculer la luminosité pour chaque pixel de l’image B, sachant que l= (r+g+b)/3,
# 4) Convertir l’image B (RGB) vers une image en niveau de gris,
# 5) Extraire le canal rouge, vert et bleu de l’image D,
# 6) Calculer le négatif (complément d’un pixel) de l’image D.


from PIL import Image

# Load the image B
img_b = Image.open("../B.jpg")

# 1) Access a given pixel in image B
x, y = 50, 50  # coordinates of the pixel to access
pixel_value = img_b.getpixel((x, y))
print(f"Pixel value at ({x}, {y}): {pixel_value}")

# 2) Modify a given pixel in image B
new_value = (255, 0, 0)  # for example, change to red
img_b.putpixel((x, y), new_value)

# 3) Calculate brightness for each pixel in image B
img_pixels = img_b.load()
width, height = img_b.size
for i in range(width):
    for j in range(height):
        r, g, b = img_pixels[i, j]
        l = (r + g + b) / 3

# 4) Convert image B (RGB) to grayscale
img_grayscale = img_b.convert("L")

# Load the image D
img_d = Image.open("../D.jpg")

# 5) Extract the red, green, and blue channels from image D
r_channel, g_channel, b_channel = img_d.split()

# 6) Calculate the negative of image D
img_pixels_d = img_d.load()  # Use the pixel data of image D
width_d, height_d = img_d.size  # Get the dimensions of image D
for i in range(width_d):
    for j in range(height_d):
        r, g, b = img_pixels_d[i, j]
        img_pixels_d[i, j] = (255 - r, 255 - g, 255 - b)


# If you want to save the changes
img_d.save('NegativeD.jpg')



