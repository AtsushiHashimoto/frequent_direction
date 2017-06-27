# -*- coding: utf-8 -*-
#!/usr/bin/env python

#####
# BSD 2-clause "Simplified" License
#####

import numpy as np
import numpy.linalg as ln
import math
import sys

""" This is a simple and deterministic method for matrix sketch.
The original method has been introduced in [Liberty2013]_ .

[Liberty2013] Edo Liberty, "Simple and Deterministic Matrix Sketching", ACM SIGKDD, 2013.
"""

class FrequentDirection:
    def __init__(self,ell):
        self.ell = ell
        self.M = None
        self.N = 0
        self.mat_b = None
        self.zero_rows = None

    def is_initialized(self):
        return (self.M is not None)

    def initialize(self,row):
        self.M = len(row)
        # Input error handling
        if math.floor(ell / 2) >= self.M:
            raise ValueError('Error: ell must be smaller than M * 2')
        self.N = 0
        # initialize output matrix B
        self.mat_b = np.zeros([ell, self.M])
        # compute zero valued row list
        self.zero_rows = np.nonzero([round(s, 7) == 0.0 for s in np.sum(self.mat_b, axis = 1)])[0].tolist()
        return

    def get_result(self, initialize=False):
        if ell >= self.N:
            raise ValueError('Error: ell must not be greater than N')
        sketch = self.mat_b
        if initialize:
            self.__init__(self.ell)
        return sketch

    def add_sample(self,row):
        if not self.is_initialized():
            self.initialize(row)

        # iteration
        i = self.N

        # insert a row into matrix B
        mat_b[self.zero_rows[0], :] = row

        # remove zero valued row from the list
        zero_rows.remove(zero_rows[0])

        # if there is no more zero valued row
        if len(zero_rows) == 0:

            # compute SVD of matrix B
            mat_u, vec_sigma, mat_v = ln.svd(self.mat_b, full_matrices=False)

            # obtain squared singular value for threshold
            squared_sv_center = vec_sigma[math.floor(self.ell / 2)] ** 2

            # update sigma to shrink the row norms
            sigma_tilda = [(0.0 if d < 0.0 else math.sqrt(d)) for d in (vec_sigma ** 2 - squared_sv_center)]

            # update matrix B where at least half rows are all zero
            self.mat_b = np.dot(np.diagflat(sigma_tilda), mat_v)

            # update the zero valued row list
            self.zero_rows = np.nonzero([round(s, 7) == 0 for s in np.sum(self.mat_b, axis = 1)])[0].tolist()
        self.N = self.N + 1


def calculateError(mat_a, mat_b):
    """Compute the degree of error by sketching

    :param mat_a: original matrix
    :param mat_b: sketch matrix
    :returns: reconstruction error
    """
    dot_mat_a = np.dot(mat_a.T, mat_a)
    dot_mat_b = np.dot(mat_b.T, mat_b)
    return ln.norm(dot_mat_a - dot_mat_b, ord = 2)


def squaredFrobeniusNorm(mat_a):
    """Compute the squared Frobenius norm of a matrix

    :param mat_a: original matrix
    :returns: squared Frobenius norm
    """
    return ln.norm(mat_a, ord = 'fro') ** 2
