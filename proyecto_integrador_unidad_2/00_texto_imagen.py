import cv2
import numpy as np

#img = cv2.imread('imagen_01.jpg')
# Construcción de imagen
img = np.ones((640,960,3), dtype=np.uint8)*255

font_name=['HERSHEY SIMPLEX',
     'HERSHEY PLAIN',
     'HERSHEY DUPLEX', 
     'HERSHEY COMPLEX', 
     'HERSHEY TRIPLEX', 
     'HERSHEY COMPLEX SMALL', 
     'HERSHEY SCRIPTSIMPLEX', 
     'HERSHEY SCRIPTCOMPLEX',
     'ITALIC' ]

fonts=[cv2.FONT_HERSHEY_SIMPLEX,
     cv2.FONT_HERSHEY_PLAIN,
     cv2.FONT_HERSHEY_DUPLEX, 
     cv2.FONT_HERSHEY_COMPLEX, 
     cv2.FONT_HERSHEY_TRIPLEX, 
     cv2.FONT_HERSHEY_COMPLEX_SMALL, 
     cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 
     cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
     cv2.FONT_ITALIC ]


# Texto en la imagen
# Nombre imagen, texto, ubicación, tipografía, canales, color, tamaño
#cv2.putText(img, 'Hola mundo', (50,100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 3)

#for i in range(5):
    #cv2.putText(img, 'Hola mundo', (25,75*(i+1)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), i+1)

for i in range(len(fonts)):
    cv2.putText(img, font_name[i], (25,50*(i+1)), fonts[i], 1.8, (0,0,0), 2)
cv2.imshow('Imagen', img)

cv2.waitKey()