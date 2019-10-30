# unsplashLink = 'https://unsplash.com'
# photoLink = 'https://unsplash.com/photos/X0xMB7cqKBI'

from Detector import Detector
from Screen import Screen

rec = Detector()
screen = Screen()
inp = None
while inp != '0':
    print("Qual tipo de detecção facial você deseja fazer?")
    print('1 - Detecção de uma foto')
    print('2 - Detecção em tempo real da webcam')
    print('0 - Encerrar')
    inp = input()
    if inp == '1':
        image = rec.recognizeFace('image-small.jpg', rec_eyes=True)
        if image is None:
            print("######################")
            print("Imagem não encontrada")
            print("######################")
        else:
            screen.showImage(image, 'image')
    elif inp == '2':
        screen.recognizeFaceInVideo()
print("Acabou")
