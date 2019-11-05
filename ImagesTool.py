# https://google-images-download.readthedocs.io/en/latest/arguments.html ## Argumentos para downloads do Google
from google_images_download import google_images_download
# from zipfile import ZipFile
import os
import cv2
import threading
class ImagesTool:

    def __init__(self):
        self.downloader = google_images_download.googleimagesdownload()

    def downloadImages(self, keywords, output_directory, limit = 10):
        arguments = {"keywords":keywords,"limit":limit, "output_directory": output_directory, "save_source": 'tree'}
        paths = self.downloader.download(arguments)
        # self.zip()

    def resizeAllImagesInDir(self, dir):
        rootPath = os.getcwd()
        if rootPath not in dir:
            dir = rootPath+"/"+dir

        pathResizedImages = dir+"/resized"
        if not os.path.exists(pathResizedImages): #Does the folder "small" exists ?
           os.makedirs(pathResizedImages) #If not, create it

        dirImages = os.listdir(dir)
        jobs = []
        leng = len(dirImages)
        x = True
        countStart = 0
        countRange = 20
        #rever
        while x:
            if countRange < leng:
                thread = threading.Thread(target=self.resizeManyImages(dirImages[countStart:countRange], dir, pathResizedImages))
                jobs.append(thread)
                countStart = countRange+1
                countRange += countRange
            else:
                thread = threading.Thread(target=self.resizeManyImages(dirImages[countStart:], dir, pathResizedImages))
                x = False
                break


        # thread = threading.Thread(target=self.resizeManyImages(dirImages[51:100], dir, pathResizedImages))
        # jobs.append(thread)
        # thread = threading.Thread(target=self.resizeManyImages(dirImages[100:150], dir, pathResizedImages))
        # jobs.append(thread)
        # thread = threading.Thread(target=self.resizeManyImages(dirImages[150:200], dir, pathResizedImages))
        # jobs.append(thread)
        # thread = threading.Thread(target=self.resizeManyImages(dirImages[250:300], dir, pathResizedImages))
        # jobs.append(thread)
        # thread = threading.Thread(target=self.resizeManyImages(dirImages[300:], dir, pathResizedImages))
        # jobs.append(thread)
        for j in jobs:
            j.start()
        for j in jobs:
            j.join()
        # self.resizeManyImages(dirImages, dir, pathResizedImages)

    def resizeManyImages(self, dirImages, dir, pathResizedImages):
        for image in dirImages:
            img=cv2.imread(dir+"/"+image)
            if img is not None:
                imResize = cv2.resize(img,(200,200))
                cv2.imwrite(pathResizedImages+"/"+image, imResize)

    # def zip(self):
    #     # specifying the zip file name
    #     file_name = "my_python_files.zip"
    #
    #     # opening the zip file in READ mode
    #     with ZipFile(file_name, 'r') as zip:
    #         # printing all the contents of the zip file
    #         zip.printdir()
    #
    #         # extracting all the files
    #         print('Extracting all the files now...')
    #         zip.extractall()
    #         print('Done!')
