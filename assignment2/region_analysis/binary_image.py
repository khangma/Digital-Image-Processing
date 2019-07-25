import numpy as np
import math

class binary_image:

    def compute_histogram(self, image):

        hist = [0]*256
        [width, height] = image.shape
        w = width
        h = height
        total = width * height
        for i in range(w):
            for j in range(h):
                index = image[i, j]
                hist[index] = hist[index] + 1

        for i in range(len(hist)):
            hist[i] = hist[i] / total

        return hist

    def find_optimal_threshold(self, hist):

        threshold = 256 // 2
        i = threshold - 1
        j = 256
        val_1 = 0.00
        val_2 = 0.00
        while True:
            exVal_1 = 0.00
            exVal_2 = 0.00
            for x in range(int(threshold)):
                exVal_1 = exVal_1 + hist[x] * float(x)
            for y in range(int(threshold), j):
                exVal_2 = exVal_2 + hist[y] * float(y)
            threshold = (exVal_1 + exVal_2)/2
            diff_1 = abs(val_1 - exVal_1)
            diff_2 = abs(val_2 - exVal_2)
            if (diff_1 == 0) and (diff_2 == 0):
                break
            else:
                val_1 = exVal_1
                val_2 = exVal_2

        return int(threshold)

    def binarize(self, image):

        bin_img = image.copy()

        hist = self.compute_histogram(image)
        threshold = self.find_optimal_threshold(hist)

        [width, height] = bin_img.shape

        for i in range(width):
            for j in range(height):
                if bin_img[i, j] < threshold:
                    bin_img[i, j] = 255
                else:
                    bin_img[i, j] = 0

        return bin_img


