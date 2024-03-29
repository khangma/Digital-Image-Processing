# For this part of the assignment, You can use inbuilt functions to compute the fourier transform
# You are welcome to use fft that are available in numpy and opencv
import numpy as np
import math
class Filtering:
    image = None
    filter = None
    cutoff = None
    order = None

    def __init__(self, image, filter_name, cutoff, order = 0):
        """initializes the variables frequency filtering on an input image
        takes as input:
        image: the input image
        filter_name: the name of the mask to use
        cutoff: the cutoff frequency of the filter
        order: the order of the filter (only for butterworth
        returns"""
        self.image = image
        if filter_name == 'ideal_l':
            self.filter = self.get_ideal_low_pass_filter
        elif filter_name == 'ideal_h':
            self.filter = self.get_ideal_high_pass_filter
        elif filter_name == 'butterworth_l':
            self.filter = self.get_butterworth_low_pass_filter
        elif filter_name == 'butterworth_h':
            self.filter = self.get_butterworth_high_pass_filter
        elif filter_name == 'gaussian_l':
            self.filter = self.get_gaussian_low_pass_filter
        elif filter_name == 'gaussian_h':
            self.filter = self.get_gaussian_high_pass_filter

        self.cutoff = cutoff
        self.order = order


    def get_ideal_low_pass_filter(self, shape, cutoff, order):
        """Computes a Ideal low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the ideal filter
        returns a ideal low pass mask"""

        P = shape[0]
        Q = shape[1]

        mask = np.zeros(shape=(P, Q))

        for u in range(P):
            for v in range(Q):

                d = np.sqrt(math.pow((u - P / 2), 2) + math.pow((v - Q / 2), 2))

                if d <= cutoff:
                    mask[u, v] = 1
                else:
                    mask[u, v] = 0

        return mask


    def get_ideal_high_pass_filter(self, shape, cutoff, order):
        """Computes a Ideal high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the ideal filter
        returns a ideal high pass mask"""

        #Hint: May be one can use the low pass filter function to get a high pass mask

        P = shape[0]
        Q = shape[1]

        mask = np.zeros(shape=(P, Q))

        for u in range(P):
            for v in range(Q):

                d = np.sqrt(math.pow((u - P / 2), 2) + math.pow((v - Q / 2), 2))

                if d <= cutoff:
                    mask[u, v] = 0
                else:
                    mask[u, v] = 1

        return mask


    def get_butterworth_low_pass_filter(self, shape, cutoff, order):
        """Computes a butterworth low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the butterworth filter
        order: the order of the butterworth filter
        returns a butterworth low pass mask"""

        P = shape[0]
        Q = shape[1]

        mask = np.zeros(shape=(P, Q))

        for u in range(P):
            for v in range(Q):

                d = np.sqrt(math.pow((u - P / 2), 2) + math.pow((v - Q / 2), 2))

                mask[u, v] = 1 / (1 + math.pow((d / cutoff), (2 * order)))

        return mask

    def get_butterworth_high_pass_filter(self, shape, cutoff, order):
        """Computes a butterworth high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the butterworth filter
        order: the order of the butterworth filter
        returns a butterworth high pass mask"""

        #Hint: May be one can use the low pass filter function to get a high pass mask

        P = shape[0]
        Q = shape[1]

        mask = np.zeros(shape=(P, Q))

        for u in range(P):
            for v in range(Q):

                d = np.sqrt(math.pow((u - P / 2), 2) + math.pow((v - Q / 2), 2))

                if d != 0:
                    mask[u, v] = 1 / (1 + math.pow((cutoff / d), (2 * order)))
                else:
                    mask[u, v] = 0;

        return mask

    def get_gaussian_low_pass_filter(self, shape, cutoff, order):
        """Computes a gaussian low pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the gaussian filter (sigma)
        returns a gaussian low pass mask"""

        P = shape[0]
        Q = shape[1]

        mask = np.zeros(shape=(P, Q))

        for u in range(P):
            for v in range(Q):

                d = np.sqrt(math.pow((u - P / 2), 2) + math.pow((v - Q / 2), 2))

                mask[u][v] = math.exp((-math.pow(d, 2)) / (2 * math.pow(cutoff, 2)))

        return mask


    def get_gaussian_high_pass_filter(self, shape, cutoff, order):
        """Computes a gaussian high pass mask
        takes as input:
        shape: the shape of the mask to be generated
        cutoff: the cutoff frequency of the gaussian filter (sigma)
        returns a gaussian high pass mask"""

        #Hint: May be one can use the low pass filter function to get a high pass mask

        P = shape[0]
        Q = shape[1]

        mask = np.zeros(shape=(P, Q))

        for u in range(P):
            for v in range(Q):

                d = np.sqrt(math.pow((u - P / 2), 2) + math.pow((v - Q / 2), 2))

                mask[u, v] = 1 - math.exp((-math.pow(d, 2)) / (2 * math.pow(cutoff, 2)))

        return mask

    def post_process_image(self, image):
        """Post process the image to create a full contrast stretch of the image
        takes as input:
        image: the image obtained from the inverse fourier transform
        return an image with full contrast stretch
        -----------------------------------------------------
        1. Full contrast stretch (fsimage)
        2. take negative (255 - fsimage)
        """

        a = np.min(image)
        b = np.max(image)
        k = 255
        [row, col] = np.shape(image)

        for i in range(row):
            for j in range(col):

                image[i, j] = (k / (b - a)) * (image[i, j] - a)

        # program might take a negative of the image when the average is too low because the image will be mostly black
        # and therefore needs to be inverted so that looking at the image is more pleasant.
        avg = np.average(image)

        if avg > 50:
            return image.astype('uint8')
        else:
            return (255 - image).astype('uint8')

    def filtering(self):
        """Performs frequency filtering on an input image
        returns a filtered image, magnitude of DFT, magnitude of filtered DFT        
        ----------------------------------------------------------
        You are allowed to used inbuilt functions to compute fft
        There are packages available in numpy as well as in opencv
        Steps:
        1. Compute the fft of the image
        2. shift the fft to center the low frequencies
        3. get the mask (write your code in functions provided above) the functions can be called by self.filter(shape, cutoff, order)
        4. filter the image frequency based on the mask (Convolution theorem)
        5. compute the inverse shift
        6. compute the inverse fourier transform
        7. compute the magnitude
        8. You will need to do a full contrast stretch on the magnitude and depending on the algorithm you may also need to
        take negative of the image to be able to view it (use post_process_image to write this code)
        Note: You do not have to do zero padding as discussed in class, the inbuilt functions takes care of that
        filtered image, magnitude of DFT, magnitude of filtered DFT: Make sure all images being returned have grey scale full contrast stretch and dtype=uint8 
        """

        # 1. compute the dft of the image
        dft = np.fft.fft2(self.image)

        # 2. shift the dft low frequencies to the center
        dft_shifted = np.fft.fftshift(dft)

        # compute magnitude of dft
        dft_mag = np.log(np.abs(dft_shifted))
        dft_mag = (255 * (dft_mag / np.max(dft_mag))).astype('uint8')

        # 3. Get the mask
        mask = self.filter(dft.shape, self.cutoff, self.order)

        # 4. filter the image based on the mask
        filtered = dft_shifted * mask

        # compute the magnitude of the filtered dft
        fil_mag = dft_mag * mask

        # 5. Compute the inverse shift
        inverse_shift = np.fft.ifftshift(filtered)

        # 6. Compute the inverse Fourier transform
        inverse_dft = np.fft.ifft2(inverse_shift)

        # 7. Compute the magnitude
        filtered_image = np.abs(inverse_dft)

        # 8. Full contrast stretch
        new_image = self.post_process_image(filtered_image)

        return [dft_mag, fil_mag, new_image]

