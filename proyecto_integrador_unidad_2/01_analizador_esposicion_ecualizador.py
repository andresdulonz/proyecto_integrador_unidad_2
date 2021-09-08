import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('imagen_sub.jpg')
img_g = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Cosntruir histograma
[M, N] = img.shape[0:2]
hist = cv2.calcHist([img_g], [0], None, [5], [0,256]).flatten()/(M*N)

# Seleccion de exposicion
max_element = np.argmax(hist)
if max_element == 4 and hist[4] > 0.3:
    img_ecu = cv2.equalizeHist(img_g)
    cv2.putText(img_ecu, 'Sobrexpuesta y ecualizada por: A.S.A', (10,30), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
    cv2.imshow('Imagen sobrexpuesta', img_ecu)
elif max_element == 0 and hist[0] > 0.3:
    img_ecu = cv2.equalizeHist(img_g)
    cv2.putText(img_ecu, 'Subexpuesta y ecualizada por: A.S.A', (10,30), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
    cv2.imshow('Imagen subexpuesta', img_ecu)
else:
    cv2.putText(img_g, 'Buena exposicion por: A.S.A', (10,30), cv2.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
    cv2.imshow('Imagen buena exposicion', img_g)

# Mostrar el histograma
fig = plt.figure('Histograma')
plt.bar(range(len(hist)), hist)
plt.show()
cv2.waitKey()