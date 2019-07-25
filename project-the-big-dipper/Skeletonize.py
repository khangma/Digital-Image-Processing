import numpy as np
import cv2
import Morphology

class Skeletonize:
    def erode(self, img):
        [w, h] = img.shape
        eroded = img.copy()
        for i in range(w-1):
            for j in range(h-1):
                if img[i][j] == 0 or img[i-1][j] == 0 or img[i+1][j] == 0 or img[i][j-1] == 0 or img[i][j+1] == 0:
                    eroded[i][j] = 0

        return eroded

    def dilate(self, img):
        [w, h] = img.shape
        dilated = img.copy()
        for i in range(w - 1):
            for j in range(h - 1):
                if img[i][j] == 255 or img[i - 1][j] == 255 or img[i + 1][j] == 255 or img[i][j - 1] == 255 or img[i][j + 1] == 255:
                    dilated[i][j] = 255

        return dilated

    def bitwise_not(self, img):
        [w, h] = img.shape
        not_img = np.zeros((w, h), dtype = 'uint8')
        for i in range(w):
            for j in range(h):
                if img[i][j] == 0:
                    not_img[i][j] = 255
        return not_img

    def subtract(self, img, mask):
        [w, h] = img.shape
        subtracted = np.zeros((w, h), dtype='uint8')
        mask = self.bitwise_not(mask)
        for i in range(w):
            for j in range(h):
                if mask[i][j] == 255 and img[i][j] == 255:
                    subtracted[i][j] = 255
        return subtracted

    def bitwise_or(self, img, mask):
        [w, h] = img.shape
        or_img = np.zeros((w, h), dtype='uint8')
        for i in range(w):
            for j in range(h):
                if mask[i][j] == 255 or img[i][j] == 255:
                    or_img[i][j] = 255

        return or_img

    def skeletonize(self, img):
        morph_obj = Morphology.Morphology()
        skeleton = np.zeros(img.shape, np.uint8)
        done = False
        while not done:
            size_before = cv2.countNonZero(img)
            eroded = morph_obj.erosion(img)
            dilated = morph_obj.dilate(eroded)
            mask = self.subtract(img, dilated)
            skeleton = self.bitwise_or(skeleton, mask)
            img = eroded.copy()
            size_after = cv2.countNonZero(img)
            print("size before: ", size_before)
            print("size after: ",size_after)
            if size_before == size_after:
                done = True

        cv2.imshow("eroded", eroded)
        cv2.imshow("skeleton", skeleton)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        return skeleton
