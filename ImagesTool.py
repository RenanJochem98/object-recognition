# https://google-images-download.readthedocs.io/en/latest/arguments.html ## Argumentos para downloads do Google
from google_images_download import google_images_download
# from zipfile import ZipFile
import os
import cv2
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
