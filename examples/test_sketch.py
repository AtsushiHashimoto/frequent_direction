# -*- coding: utf-8 -*-
import time

from numpy.random import *
from frequent_direction import FrequentDirection, calculateError, squaredFrobeniusNorm


@profile
def main():

    mat_rand = rand(1000,256) # 256 dimensional 1000 samples
    mat_rand = mat_rand.T # transpose for SVD
    fd = FrequentDirection(32) # compress to 32 dimensional samples

    start = time.time()
    print("trial start")
    for row in mat_rand:
        fd.add_sample(row)
    mat_sketch = fd.get_result()
    elapsed_time = time.time() - start
    print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")
    print("Original Matrix Shape:", mat_rand.shape)
    print("Sketched Matrix Shape:", mat_sketch.shape)
    error = calculateError(mat_rand,mat_sketch)
    flobius_norm =  squaredFrobeniusNorm(mat_rand)
    print("Error: %f"%error)
    print("Error Upper bound: %f"%(flobius_norm*2))

if __name__ == "__main__":
    # execute only if run as a script
    main()
