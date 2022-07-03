import numpy as np
import time
from biclustlib.algorithms import ChengChurchAlgorithm
from biclustlib.algorithms import SecuredChengChurchAlgorithm
from biclustlib.datasets import synthetic

m0 = time.perf_counter()

# load synthetic data set
data, predicted = synthetic.make_const_data()

# creating an instance of the SeCCA ChengChurchAlgorithm class and running with the parameters of the original study
secca= SecuredChengChurchAlgorithm(num_biclusters=100, msr_threshold=300.0, multiple_node_deletion_threshold=1.2)
biclustering = secca.run(data)
print(biclustering)

m1 = time.perf_counter()
print("Time Performance in Calculating Homomorphically: ", round(m1 - m0, 5), "Seconds")

