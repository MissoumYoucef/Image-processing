from PIL import Image, ImageFilter, ImageChops
import numpy as np

# 1. Read an image in color
image = Image.open("../F.jpg")

# 2. Display the image
image.show()

# 3. Print the format, dimensions, and representation mode of the image
width, height = image.size
print(f"Dimensions: {width}x{height}")
print(f"Mode: {image.mode}")

# 4. Display the red, green, and blue channels
r, g, b = image.split()
r.show("Red Channel")
g.show("Green Channel")
b.show("Blue Channel")

# 5. Convert image to grayscale
img_gris = image.convert("L")
img_gris.show("Grayscale Image")

# 6. Find the inverse image
img_inverse = ImageChops.invert(img_gris)
img_inverse.show("Inverse Image")

# 7. Save the inverse image
img_inverse.save('ImgInverse.jpg')

# 8. Filter the images using the mentioned filters

# Mean filter
img_mean = img_gris.filter(ImageFilter.BoxBlur(5))
img_mean.show("Mean Filter")

# Median filter
img_median = img_gris.filter(ImageFilter.MedianFilter(5))
img_median.show("Median Filter")

# Maximum filter
# For Maximum filter with Pillow, we need to use ImageFilter.MaxFilter
img_maximum = img_gris.filter(ImageFilter.MaxFilter(5))
img_maximum.show("Maximum Filter")

# Minimum filter
# For Minimum filter with Pillow, we need to use ImageFilter.MinFilter
img_minimum = img_gris.filter(ImageFilter.MinFilter(5))
img_minimum.show("Minimum Filter")








# import cv2
# import numpy as np

# # 1. Read an image in color
# image = cv2.imread("A.jpg", cv2.IMREAD_COLOR)

# # 2. Display the image
# cv2.imshow('Original Image', image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 3. Print the format, dimensions, and representation mode of the image
# height, width, channels = image.shape
# print(f"Dimensions: {width}x{height}")
# print(f"Channels: {channels}")

# # 4. Display the red, green, and blue channels
# red_channel = image[:,:,2]
# green_channel = image[:,:,1]
# blue_channel = image[:,:,0]

# cv2.imshow('Red Channel', red_channel)
# cv2.imshow('Green Channel', green_channel)
# cv2.imshow('Blue Channel', blue_channel)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 5. Convert image to grayscale
# img_gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grayscale Image', img_gris)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 6. Find the inverse image
# img_inverse = 255 - img_gris
# cv2.imshow('Inverse Image', img_inverse)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # 7. Save the inverse image
# cv2.imwrite('ImgInverse.jpg', img_inverse)

# # 8. Filter the images using the mentioned filters
# # Mean filter
# img_mean = cv2.blur(img_gris, (5,5))
# cv2.imshow('Mean Filter', img_mean)

# # Median filter
# img_median = cv2.medianBlur(img_gris, 5)
# cv2.imshow('Median Filter', img_median)

# # Maximum filter
# kernel = np.ones((5,5),np.uint8)
# img_maximum = cv2.dilate(img_gris, kernel, iterations = 1)
# cv2.imshow('Maximum Filter', img_maximum)

# # Minimum filter
# img_minimum = cv2.erode(img_gris, kernel, iterations = 1)
# cv2.imshow('Minimum Filter', img_minimum)

# cv2.waitKey(0)
# cv2.destroyAllWindows()