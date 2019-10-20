# unsplashLink = 'https://unsplash.com'
# photoLink = 'https://unsplash.com/photos/X0xMB7cqKBI'

import numpy as np
import cv2 as cv

face_classifier = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
# print(type(face_classifier))
print("Lendo imagem")
image = cv.imread('image.jpg')
print("Convertendo imagem em cinza")
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

print("Detectando Escalas a imagem em cinza")
faces = face_classifier.detectMultiScale(image_gray, 1.3, 5)
# print("Formando retangulo na imagem")
# for (x,y,w,h) in faces:
#     cv.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)
#
cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()
print("Acabou")
