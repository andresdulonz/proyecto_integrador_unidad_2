import cv2
import numpy as np
import matplotlib.pyplot as plt

#img = cv2.imread('imagen_03.jpg', 0)
im = cv2.imread('imagen_02.jpg')
img = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# Normalización del histograma por su tamaño
[M, N] = img.shape[0:2]

# Características del histograma: images, channels, mask, histSize, ranges, hist=..., accumulate=...)
# Arreglo de una dimención: .flatten()
# Separación en quitiles
hist = cv2.calcHist([img], [0], None, [5], [0,256]).flatten()/(M*N)

max_element = np.argmax(hist)
if max_element == 4 and hist[4] > 0.3:
    print('Sobrexpuesta')
elif max_element == 0 and hist[0] > 0.3:
    print('Subexpuesta')
else:
    print('Buena exposicion')

cv2.imshow('Imagen', img)

# Mostrar el histograma
fig = plt.figure()
plt.bar(range(len(hist)), hist)
plt.show()

cv2.waitKey()