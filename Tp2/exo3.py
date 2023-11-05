# Exercice 3 :
# En utilisant l’’image R.jpg, écrire un script python en utilisant la bibliothèque PIL pour :
# 1. Appliquer une symétrie par rapport à la moitié des lignes de l’image R
# 2. Appliquer une symétrie par rapport à la moitié des colonnes de l’image R
# 3. Appliquer une rotation de 90° de l’image R.jpg.

from PIL import Image

# Charger l'image R.jpg
image_R = Image.open("../B.jpg")


image_R.show()
# 1. Appliquer une symétrie par rapport à la moitié des lignes
symmetry_horizontal = image_R.transpose(Image.FLIP_TOP_BOTTOM)

# 2. Appliquer une symétrie par rapport à la moitié des colonnes
symmetry_vertical = image_R.transpose(Image.FLIP_LEFT_RIGHT)

# 3. Appliquer une rotation de 90°
rotation_90_degrees = image_R.transpose(Image.ROTATE_90)

# Afficher les images résultantes
symmetry_horizontal.show()
symmetry_vertical.show()
rotation_90_degrees.show()
