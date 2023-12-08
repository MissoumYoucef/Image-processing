from PIL import Image

# Étape 1: Calculer la matrice (E) à partir de la matrice (A)
matrice_A = [[1, 2], [3, 4]]
matrice_E = []

for ligne in matrice_A:
    nouvelle_ligne = []
    for valeur in ligne:
        nouvelle_ligne.extend([valeur, valeur])
        print(nouvelle_ligne)  # Dupliquer horizontalement
    matrice_E.extend([nouvelle_ligne, nouvelle_ligne])
    print(matrice_E)  # Dupliquer verticalement


print("Matrice E:")
for ligne in matrice_E:
    print(ligne)


# Étape 2: Appliquer ce principe de mise en échelle sur l'image R.jpg
image = Image.open('../B.jpg')
largeur, hauteur = image.size
nouvelle_largeur = largeur * 4
nouvelle_hauteur = hauteur * 4
image_redimensionnee = image.resize((nouvelle_largeur, nouvelle_hauteur), Image.NEAREST)
image_redimensionnee.save('R_agrandi.jpg')

print("L'image a été agrandie avec succès et sauvegardée sous le nom 'R_agrandi.jpg'")