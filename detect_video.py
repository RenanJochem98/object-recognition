# unsplashLink = 'https://unsplash.com'
# photoLink = 'https://unsplash.com/photos/X0xMB7cqKBI'

import cv2 as cv
pathOpenCVClassifiers = "/home/renanj/.local/lib/python3.6/site-packages/cv2/data"
# pathOpenCVClassifiers = "C:/Users/Renan/AppData/Local/Programs/Python/Python36/Lib/site-packages/cv2/data"

face_classifier = cv.CascadeClassifier(pathOpenCVClassifiers+'/haarcascade_frontalface_default.xml')

captura = cv.VideoCapture(0)

while(1):
    ret, frame = captura.read()
    image_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(image_gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    cv.imshow("Video", frame)

    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

captura.release()
cv.destroyAllWindows()

print("Acabou")
