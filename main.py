# unsplashLink = 'https://unsplash.com'
# photoLink = 'https://unsplash.com/photos/X0xMB7cqKBI'

import numpy as np
import cv2 as cv

# caminho com xml dos treinamentos do OpenCV. (Features de Haar)
# pathOpenCVClassifiers = "/home/renanj/.local/lib/python3.6/site-packages/cv2/data"
pathOpenCVClassifiers = "C:/Users/Renan/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data"

face_classifier = cv.CascadeClassifier(pathOpenCVClassifiers+'/haarcascade_frontalface_default.xml')
eye_classifier = cv.CascadeClassifier(pathOpenCVClassifiers+'/haarcascade_eye.xml')
# print(type(face_classifier))
print("Lendo imagem")
# image = cv.imread('image.jpg')
image = cv.imread('image-small.jpg')
print("Convertendo imagem em cinza")
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

print("Detectando Escalas a imagem em cinza")
faces = face_classifier.detectMultiScale(image_gray, 1.3, 5)
print("Formando retangulo na imagem")
for (x,y,w,h) in faces:
    cv.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)
    roi_gray = image_gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye_classifier.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        cv.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)

cv.imshow('image', image)
cv.waitKey(0)
cv.destroyAllWindows()
print("Acabou")
