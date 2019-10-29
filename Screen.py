import cv2
from Recognizer import Recognizer
class Screen:

    def __init__(self):
        self.recognizer = Recognizer()

    def showImage(self, image, type, close_windows=True):
        cv2.imshow(type, image)
        if close_windows:
            cv2.waitKey(0)
            cv2.destroyAllWindows()

    def recognizeFaceInVideo(self):
        captura = cv2.VideoCapture(0)
        while(1):
            ret, frame = captura.read()
            # if not ret:
            #     continue
            frame = self.recognizer.recognizeFace(frame, True)
            self.showImage(frame, 'Video', close_windows=False)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break

        captura.release()
        cv2.destroyAllWindows()
