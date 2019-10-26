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
# O reconhecimento funciona com imagens em escala de preto e branco
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

print("Detectando Escalas a imagem em cinza")
# Primeiro parametro: Imagem em preto e branco
# Segundo parametro: Indica a reducao da imagem durante a verificacao.
#                    Serve verificar fotos de perto, medio distancia  ou longe
#                    1.3 eh um valor chave (Ainda nao sei porque)
# Terceiro parametro: Numero de vizinhos cada candidato a face tem.
#                     Quanto maior, mais vizinhos sao necessarios para que um local seja considerado uma face
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
