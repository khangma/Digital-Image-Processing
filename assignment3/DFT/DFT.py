# For this part of the assignment, please implement your own code for all computations,
# Do not use inbuilt functions like fft from either numpy, opencv or other libraries

import numpy as np
import math
class DFT:

    def forward_transform(self, matrix):
        """Computes the forward Fourier transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a complex matrix representing fourier transform"""

        comp_num = complex(0, 1)

        [row, col] = np.shape(matrix)
        new_matrix = np.zeros((row, col), dtype = complex)

        for u in range(row):
            for v in range(col):

                for i in range(row):
                    for j in range(col):
                        cosine = math.cos((2 * math.pi / row) * (u*i + v*j))
                        sine = comp_num * math.sin((2 * math.pi/col) * (u*i + v*j))

                        new_matrix[u, v] = new_matrix[u, v] + (matrix[i,j] * (cosine - sine))

        return new_matrix

    def inverse_transform(self, matrix):
        """Computes the inverse Fourier transform of the input matrix
        matrix: a 2d matrix (DFT) usually complex
        takes as input:
        returns a complex matrix representing the inverse fourier transform"""

        comp_num = complex(0, 1)

        [row, col] = np.shape(matrix)
        new_matrix = np.zeros((row, col), dtype=complex)

        for u in range(row):
            for v in range(col):

                for i in range(row):
                    for j in range(col):
                        cosine = math.cos((2 * math.pi / row) * (u * i + v * j))
                        sine = comp_num * math.sin((2 * math.pi / col) * (u * i + v * j))

                        new_matrix[u, v] = new_matrix[u, v] + (matrix[i, j] * (cosine + sine))

        return new_matrix


    def discrete_cosine_tranform(self, matrix):
        """Computes the discrete cosine transform of the input matrix
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing discrete cosine transform"""

        [row, col] = np.shape(matrix)
        new_matrix = np.zeros((row, col), dtype = 'uint8')

        for u in range(row):
            for v in range(col):

                for i in range(row):
                    for j in range(col):
                        cosine = math.cos((2 * math.pi / row) * (u * i + v * j))
                        new_matrix[u, v] = new_matrix[u, v] + ( matrix[i, j] * (cosine) )

        return new_matrix


    def magnitude(self, matrix):
        """Computes the magnitude of the DFT
        takes as input:
        matrix: a 2d matrix
        returns a matrix representing magnitude of the dft"""
        [row, col] = np.shape(matrix)
        new_matrix = np.zeros((row, col), dtype = 'uint8')
        for i in range(row):
            for j in range(col):
                new_matrix[i, j] = math.sqrt(math.pow(matrix[i, j].real, 2) + math.pow(matrix[i, j].imag, 2))



        return new_matrix