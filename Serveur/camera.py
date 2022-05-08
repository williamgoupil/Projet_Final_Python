import os
import time

# Pi Camera semble être un objet qui existe deja dans une librairie python, il faudrait le tester
# On est p-e pas obliger de faire un objet dans un objet.

from picamera import PiCamera

class Camera :
    def __init__(self):
        self.camera = PiCamera()

    # capture l'image et la sauvegarde dans un dossier /img/
    def capture(self):
        self.camera.start_preview()
        self.camera.capture('./img/image.jpeg')
        self.camera.stop_preview()

    # enleve l'image en mémoire pour garder seulement la derniere img ?
    def removeImg(self, path, imgName):
        os.remove(path + '/' + imgName)
        if os.path.exist(path + '/' + imgName):
            return True