# -*- coding: utf-8 -*-
import time

from numpy.random import *
from sklearn.metrics.pairwise import pairwise_kernels

from spectral_embedding_with_frequent_direction import spectral_embedding

rand_mat = rand(10000,100)
W = pairwise_kernels(rand_mat)

def trial(W,n_components,eigen_solver,use_matrix_sketch):
    start = time.time()
    print("trial start for %s"%eigen_solver)
    W_embedded = spectral_embedding(W, n_components=n_components, eigen_solver=eigen_solver,
                       random_state=None, eigen_tol=0.0,
                       norm_laplacian=True, drop_first=True, use_matrix_sketch=use_matrix_sketch)
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print(W_embedded.shape)
    return W_embedded

@profile
def main():
    W_embedded = trial(W,100,'arpack',use_matrix_sketch=True) # spectral_embedding by frequent_direction
    print(W_embedded)

    #W_embedded = trial(W,100,'amg') # brute force 1
    #print(W_embedded)

    W_embedded = trial(W,100,'arpack',use_matrix_sketch=False) # brute force 2
    print(W_embedded)

main()
