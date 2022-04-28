# SeCCA
Secured Cheng and Church Algorithm performs encrypted computations such as sum, or matrix multiplication in Python for biclustering algorithm under the MIT license.

## Installation
First you need to ensure that all packages have been installed.
+ numpy~=1.22.3
+ setuptools~=60.2.0
+ pandas~=1.4.2
+ scikit-learn~=1.0.2
+ Pyfhel~=2.3.1
+ Bottleneck~=1.3.4
+ matplotlib~=3.5.1
+ scipy~=1.8.0
+ munkres~=1.1.4

## Biclustering Algorithm
[Cheng and Church's Algorithm (CCA)](https://www.researchgate.net/profile/George_Church/publication/2329589_Biclustering_of_Expression_Data/links/550c04030cf2063799394f5e.pdf);

## Gene Expression Data Set

 *Saccharomyces cerevisiae* microarray dataset from [Tavazoie et al. (1999)](http://www.alterlab.org/teaching/BIOEN3070/papers/Tavazoie_1999.pdf) which was used in [(Cheng and Church, 2000)](https://www.researchgate.net/profile/George_Church/publication/2329589_Biclustering_of_Expression_Data/links/550c04030cf2063799394f5e.pdf);

## External Evaluation Measure

Clustering Error (CE) measure that was proposed by [Patrikainen and Meila (2006)](http://ieeexplore.ieee.org/abstract/document/1637417/);

## Example of Cheng and Church Algorithm (CCA)

```python
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
```
## Example of Secured Cheng and Church Algorithm (SeCCA)

```python
import time
from biclustlib.algorithms import SecuredChengChurchAlgorithm
from biclustlib.datasets import load_yeast_tavazoie
import numpy as np

m0 = time.perf_counter()

# load yeast data used in the original Cheng and Church's paper
data = load_yeast_tavazoie().values

# missing value imputation suggested by Cheng and Church
missing = np.where(data < 0.0)
data[missing] = np.random.randint(low=0, high=800, size=len(missing[0]))

# creating an instance of the SecuredChengChurchAlgorithm class and running with the parameters
secca = SecuredChengChurchAlgorithm(num_biclusters=5, msr_threshold=300.0, multiple_node_deletion_threshold=1.2)
biclustering = secca.run(data)
print(biclustering)

m1 = time.perf_counter()
print("Time Performance in Calculating Homomorphically: ", round(m1 - m0, 5), "Seconds")
```
