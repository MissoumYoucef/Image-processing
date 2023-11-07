
from PIL import Image, ImageEnhance, ImageOps
import numpy as np

# 1. Lire une image (A)
imgA = Image.open("../A1.jpg")
imgB = Image.open("../B1.jpg")

# 2. Afficher le format, les dimensions et le mode de représentation de l’image A.
print(imgA.format, imgA.size, imgA.mode)

# 3. Appliquer la transformation linéaire des niveaux de gris
def transform_linear(img, k=1, d=50):
    arr = np.asarray(img)
    arr = k * arr + d
    arr = np.clip(arr, 0, 255).astype(np.uint8)
    return Image.fromarray(arr)

imgA_transformed = transform_linear(imgA)

# 4. Calculer l'image inverse de (A)
def inverse_image(img):
    arr = np.asarray(img)
    arr = 255 - arr
    return Image.fromarray(arr)

imgA_inverse = inverse_image(imgA)

# 5. Appliquer la transformation logarithmique
def log_transform(img, c=255/np.log(256)):
    arr = np.asarray(img)
    arr = c * np.log1p(arr)
    arr = np.clip(arr, 0, 255).astype(np.uint8)
    return Image.fromarray(arr)

imgB_log = log_transform(imgB)

# 6. Appliquer la correction de gamma
def gamma_correction(img, gamma, c=255):
    enhancer = ImageEnhance.Brightness(img)
    return enhancer.enhance(gamma)

gamma_values = [0.2, 0.4, 1.5, 2.5]
gamma_images = [gamma_correction(imgB, gamma) for gamma in gamma_values]

# 7. Appliquer l’ajustement de contraste
def contrast_adjustment(img):
    return ImageOps.autocontrast(img)

imgA_contrast = contrast_adjustment(imgA)

# 8. Tracer l’histogramme des trois canaux après l’ajustement de contraste.
# 9. Calculer l’histogramme cumulé des trois canaux après l’ajustement de contraste.
# Pour ces tâches, vous auriez besoin de bibliothèques supplémentaires comme matplotlib ou OpenCV.

# Sauvegarde des images transformées pour visualisation
imgA_transformed.save("imgA_transformed.jpg")
imgA_inverse.save("imgA_inverse.jpg")
imgB_log.save("imgB_log.jpg")
for i, img in enumerate(gamma_images):
    img.save(f"gamma_img{i+1}.jpg")
imgA_contrast.save("imgA_contrast.jpg")


