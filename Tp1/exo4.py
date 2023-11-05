# Exercice 4 :
# Ecrire un script qui affiche une nouvelle image correspondant à l'image deux fois plus grande.


from PIL import Image

# Ouvrir l'image originale
image_originale = Image.open("../A.jpg")
image_originale.show()

# Obtenir la taille de l'image originale
largeur, hauteur = image_originale.size

# Créer une nouvelle image deux fois plus grande
nouvelle_largeur = largeur * 2
nouvelle_hauteur = hauteur * 2
nouvelle_image = Image.new("RGB", (nouvelle_largeur, nouvelle_hauteur))

# Copier l'image originale dans la nouvelle image agrandie
for y in range(nouvelle_hauteur):
    for x in range(nouvelle_largeur):
        pixel = image_originale.getpixel((x // 2, y // 2))
        nouvelle_image.putpixel((x, y), pixel)

# Afficher la nouvelle image agrandie
nouvelle_image.show()

