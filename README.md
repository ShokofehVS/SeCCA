# SeCCA
**SeCCA**: **Se**cured **C**heng and **C**hurch **A**lgorithm: privacy-preserving gene expression data analysis by biclustering algorithm -- Cheng and Church algorithm -- over yeast Saccharomyces cerevisiae cell cycle performing Homomorphic Encryption operations such as sum, or matrix multiplication in Python under the MIT license.
We apply [Pyfhel](https://pyfhel.readthedocs.io/en/latest/) as a python wrapper for the Microsoft SEAL library. 

## Installation
First you need to ensure that all packages have been installed.
+ See `requirements.txt`
+ numpy>=1.22.3
+ setuptools>=60.2.0
+ pandas>=1.4.2
+ scikit-learn>=1.0.2
+ Pyfhel>=2.3.1
+ Bottleneck>=1.3.4
+ matplotlib>=3.5.2
+ scipy>=1.8.0
+ munkres>=1.1.4

You can clone this repository:

	   > git clone https://github.com/ShokofehVS/SeCCA.git

If you miss something you can simply type:

	   > pip install -r requirements.txt

If you have all dependencies installed:

	   > python setup.py install

To install Pyfhel, on Linux,`gcc6` for Python (`3.5+`) should be installed. (more information regarding [installation of Pyfhel ](https://github.com/ibarrond/Pyfhel))

	   > apt install gcc 

## Biclustering Algorithm
Biclustering or simultaneous clustering of both genes and conditions as a new paradigm was introduced by [Cheng and Church's Algorithm (CCA)](https://www.researchgate.net/profile/George_Church/publication/2329589_Biclustering_of_Expression_Data/links/550c04030cf2063799394f5e.pdf). The concept of bicluster refers to a subset of
genes and a subset of conditions with a high similarity score, which measures the coherence of the genes and conditions in the bicluster. It also returns the list of biclusters for the given data set. 

## Gene Expression Data Set
Our input data is *yeast Saccharomyces cerevisiae cell cycle* taken from [Tavazoie et al. (1999)](https://pubmed.ncbi.nlm.nih.gov/10391217/) which was used in the orginal study by [Cheng and Church](https://www.researchgate.net/profile/George_Church/publication/2329589_Biclustering_of_Expression_Data/links/550c04030cf2063799394f5e.pdf);

## External Evaluation Measure
To measure the similarity of encrypted biclusters with non-encrypted version, we use Clustering Error (CE) as an external evaluation measure that was proposed by [Patrikainen and Meila (2006)](http://ieeexplore.ieee.org/abstract/document/1637417/);
         
## Example of Cheng and Church Algorithm (CCA)
To run the sample implementation of Cheng and Church algorithm:

	   > python3 cheng_church_yeast.py 

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
To run the sample implementation of Secured version of Cheng and Church algorithm:

	   > python3 secured_cheng_church_yeast.py  

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
