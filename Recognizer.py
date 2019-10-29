import cv2
import os
class Recognizer:

    def __init__(self):
        # caminho com xml dos treinamentos do OpenCV. (Features de Haar)
        self.pathOpenCVClassifiers = "C:/Users/Renan/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data"

        if os.name == 'posix':
            self.pathOpenCVClassifiers = "/home/renanj/.local/lib/python3.6/site-packages/cv2/data"

    def recognizeFace(self, image, rec_eyes = False):
        if isinstance(image, str):
            image = cv2.imread(image)
        if image is not None:
            face_classifier = cv2.CascadeClassifier(self.pathOpenCVClassifiers+'/haarcascade_frontalface_default.xml')
            eye_classifier = cv2.CascadeClassifier(self.pathOpenCVClassifiers+'/haarcascade_eye.xml')
            # O reconhecimento funciona com imagens em escala de preto e branco
            image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            # Primeiro parametro: Imagem em preto e branco
            # Segundo parametro: Indica a reducao da imagem durante a verificacao.
            #                    Serve verificar fotos de perto, medio distancia  ou longe
            #                    1.3 eh um valor chave (Ainda nao sei porque)
            # Terceiro parametro: Numero de vizinhos cada candidato a face tem.
            #                     Quanto maior, mais vizinhos sao necessarios para que um local seja considerado uma face
            faces = face_classifier.detectMultiScale(image_gray, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(image, (x,y), (x+w, y+h), (255,0,0), 2)
                if rec_eyes:
                    roi_gray = image_gray[y:y+h, x:x+w]
                    roi_color = image[y:y+h, x:x+w]
                    eyes = eye_classifier.detectMultiScale(roi_gray)
                    for (ex,ey,ew,eh) in eyes:
                        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0,255,0), 2)

        return image
