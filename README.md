# spectral_embedding4large_scale_matrix
memory efficient spectral embedding

# install
    % pip install git+https://github.com/AtsushiHashimoto/spectral_embedding4large_scale_matrix.git

# examples
1. short instruction
```
from spectral_embedding_with_frequent_direction import spectral_embedding
...
# use_matrix_sketch = True for reduce memory consumption, otherwise it works as that of sklearn.
W_embedded = spectral_embedding(W, n_components=n_components, eigen_solver='arpack',\
                       random_state=None, eigen_tol=0.0,\
                       norm_laplacian=True, drop_first=True, use_matrix_sketch=True) 
```
2. [source code is here](./examples/test_embedding.py)
3. how to execute
```
    % pip install psutil
    % pip install memory_profiler
    % python -m memory_profiler test_embedding.py
```

# result of a sample execution.
with matrix sketch => 71.671 MiB for 10000x10000 graph laplacian
without => 865.652 MiB

```
Filename: test_embedding.py

Line #    Mem usage    Increment   Line Contents
================================================
25  835.688 MiB    0.000 MiB   @profile
26                             def main():
27   71.691 MiB -763.996 MiB       W_embedded = trial(W,100,'arpack',use_matrix_sketch=True) # spectral_embedding by frequent_direction
28   72.414 MiB    0.723 MiB       print(W_embedded)
29                             
30                                 #W_embedded = trial(W,100,'amg') # brute force 1
31                                 #print(W_embedded)
32                             
33  865.652 MiB  793.238 MiB       W_embedded = trial(W,100,'arpack',use_matrix_sketch=False) # brute force 2
34  865.664 MiB    0.012 MiB       print(W_embedded)
```
