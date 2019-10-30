# https://google-images-download.readthedocs.io/en/latest/arguments.html ## Argumentos para downloads do Google
from google_images_download import google_images_download
# from zipfile import ZipFile
class ImagesTool:

    def __init__(self):
        self.downloader = google_images_download.googleimagesdownload()

    def downloadImages(self, keywords, output_directory, limit = 10):
        arguments = {"keywords":keywords,"limit":limit, "output_directory": output_directory, "save_source": 'tree'}
        paths = self.downloader.download(arguments)
        # self.zip()

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
