from resize.interpolation import interpolation
import numpy
import math

class resample:
    def resize(self, image, fx=None, fy=None, interpolation=None):
        """calls the appropriate funciton to resample an image based on the interpolation method
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        interpolation: method used for interpolation ('either bilinear or nearest_neighbor)
        returns a resized image based on the interpolation method
        """
        if interpolation == 'bilinear':
            return self.bilinear_interpolation(image, float(fx), float(fy))

        elif interpolation == 'nearest_neighbor':
            return self.nearest_neighbor(image, float(fx), float(fy))

    def nearest_neighbor(self, image, fx, fy):
        """resizes an image using nearest neighbor approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the nearest neighbor interpolation method
        """

        # write your code for nearest neighbor here
        [width, height] = image.shape       # get dimension of the image
        w = int(width*fx)                   # calculate new width
        h = int(height*fy)                  # calculate new height
        new_image = numpy.zeros((w, h), dtype='uint8')      # create new blank image
        for x in range(w):
            for y in range(h):
                new_image[x][y] = image[int(x/fx), int(y/fy)]



        return new_image

    def bilinear_interpolation(self, image, fx, fy):
        """resizes an image using bilinear interpolation approximation for resampling
        image: the image to be resampled
        fx: scale along x direction (eg. 0.5, 1.5, 2.5)
        fx: scale along y direction (eg. 0.5, 1.5, 2.5)
        returns a resized image based on the bi-linear interpolation method
        """

        # Write your code for bi-linear interpolation here
        [width, height] = image.shape       # get dimensions of the image
        w = int(width * fx)                 # calculate new width
        h = int(height * fy)                # calculate new height
        new_image = numpy.zeros((w, h), dtype='uint8')
        intrp = interpolation()
        for x in range(w):
            for y in range(h):
                i = int(x/fx)
                j = int(y/fy)
                if (i+1) >= width:
                    i = i-1
                elif (j+1) >= height:
                    j = j-1
                pt1 = [i, j, image[i, j]]               # Q11
                pt2 = [i+1, j, image[i+1, j]]           # Q21
                pt3 = [i, j+1, image[i, j+1]]           # Q12
                pt4 = [i+1, j+1, image[i+1, j+1]]       # Q22
                unknown = [(x/fx), (y/fy)]
                result = intrp.bilinear_interpolation(pt1, pt2, pt3, pt4, unknown)
                new_image[x][y] = result

        return new_image
