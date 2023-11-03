# Exercice 2 :
# Ecrire un script python qui affiche l’image A avec seulement deux couleurs : le noir et le blanc.

from PIL import Image

# Load the image
image = Image.open("../A.jpg")

# Convert the image to grayscale
img_gris = image.convert("L")

# Threshold the image to get a binary image (black and white)
threshold = 128  # This is a standard value. Adjust as needed.
binary_image = img_gris.point(lambda p: 255 if p > threshold else 0)

# Display the binary image
binary_image.show()

# If you want to save the binary image
binary_image.save('BinaryImage.jpg')


