from ImagesTool import ImagesTool
class Model:

    def __init__(self):
        self.imageTool = ImagesTool()
        self.defaultImagesPath = 'images'
        self.limitImagesToModel = 5

    def createModelImagesBase(self, keywords):
        self.imageTool.downloadImages(keywords, self.defaultImagesPath, self.limitImagesToModel)
        # define and resize images
        # verify if need change to scale gray

    def refineModelImagesBase(self):
        pass
        # delete out of scope images
        # delete repeated images

    def zipImages(self):
        pass
        # to Decrease memory size of program

    def train(self):
        pass

    def sendImagesToCloud(self):
        pass
