import cv2
import numpy as np
import math

class BoundaryExtraction:

    #compute the eroded image
    def erodeImage(self, image):
        count = int(image.shape[0])*int(image.shape[1])
        testcount=0
        erodedImage = image.copy()

        for i in range(1, image.shape[0]-1):
            for j in range(1, image.shape[1]-1):
                if image[i-1][j]== 0 or image[i+1][j]== 0 or image[i][j-1]== 0 or image[i][j+1]== 0 or image[i][j] == 0:
                    erodedImage[i][j] = 0
                    testcount += 1

        return erodedImage

    def subtractImages(self, erodedImage, originalImage):
        q = erodedImage.shape[0]
        w = erodedImage.shape[1]
        subtractedImageArray = np.zeros([q, w])
        count = 0
        for i in range(1, erodedImage.shape[0]-1):
            for j in range(1, erodedImage.shape[1]-1):
                if(erodedImage[i][j] - originalImage[i][j] !=0):
                    subtractedImageArray[i][j]= 255
                    count+=1

        return subtractedImageArray










