# -*- coding: utf-8 -*-
import time
import memory_profiler

from numpy.random import *
from frequent_direction import FrequentDirection


@profile
def __main__():

    rand_mat = rand(1000,100)
    fd = FrequentDirection(20)

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
