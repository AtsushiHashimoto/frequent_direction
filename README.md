# frequent-direction

Implementation of Frequent-directions algorithm for efficient matrix sketching [Liberty2013]_ .

# Install
```
% pip install git+https://github.com/AtsushiHashimoto/frequent_direction.git
```

# Sample Code
```
% wget https://raw.githubusercontent.com/AtsushiHashimoto/frequent_direction/master/examples/test_sketch.py
% pip install memory_profiler
% python -m memory_profiler test_sketch.py
```

# Usage
```
import frequent_direction
import csv

ell = 20 # sketch an N x M as an N x ell mat.
fd = frequent_direction(ell)
with open("large_scale_matrix.csv","r") as fin:
  reader = csv.reader(fin)
  for row in reader:
    fd.add_sample(row)

mat_b = fd.get_result()
print(mat_b.shape)
print(mat_b)
```

# License
BSD 2-clause "Simplified" License

# Original connected_nodes
1. [codes by authors](https://github.com/edoliberty/frequent-directions)
2. [codes by hido](https://github.com/hido/frequent-direction) <- this project is a rearrangement of this code.

# Reference
 [Liberty2013]  Edo. Liberty, "Simple and Deterministic Matrix Sketching", ACM SIGKDD, 2013. http://www.cs.yale.edu/homes/el327/papers/simpleMatrixSketching.pdf
