import time
from biclustlib.algorithms import ChengChurchAlgorithm
from biclustlib.datasets import load_yeast_tavazoie
import numpy as np

m0 = time.perf_counter()

# load yeast data used in the original Cheng and Church's paper
data = load_yeast_tavazoie().values

# missing value imputation suggested by Cheng and Church
missing = np.where(data < 0.0)
data[missing] = np.random.randint(low=0, high=800, size=len(missing[0]))

# creating an instance of the ChengChurchAlgorithm class and running with the parameters
cca = ChengChurchAlgorithm(num_biclusters=5, msr_threshold=300.0, multiple_node_deletion_threshold=1.2)
biclustering = cca.run(data)
print(biclustering)

m1 = time.perf_counter()
print("Time Performance in Original Algorithm: ", round(m1 - m0, 5), "Seconds")


