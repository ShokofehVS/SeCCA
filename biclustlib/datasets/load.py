"""
    SeCCA: A Python library of privacy-preserved biclustering algorithm (Cheng and Church) with Homomorphic Encryption

    Copyright (C) 2022  Shokofeh VahidianSadegh

    This file is part of SeCCA.

"""

from os.path import dirname, join
import numpy as np
import pandas as pd

def load_yeast_tavazoie():
    """Load and return the yeast dataset (Tavazoie et al., 2000) used in the original biclustering study
    of Cheng and Church (2000) as a pandas.DataFrame. All elements equal to -1 are missing values. This
    dataset is freely available in http://arep.med.harvard.edu/biclustering/.

    Reference
    ---------
    Cheng, Y., & Church, G. M. (2000). Biclustering of expression data. In Ismb (Vol. 8, No. 2000, pp. 93-103).

    Tavazoie, S., Hughes, J. D., Campbell, M. J., Cho, R. J., & Church, G. M. (1999). Systematic determination of genetic
    network architecture. Nature genetics, 22(3), 281-285.
    """
    module_dir = dirname(__file__)
    data = np.loadtxt(join(module_dir, 'data', 'yeast_tavazoie', 'yeast_tavazoie.txt'), dtype=np.double)
    genes = np.loadtxt(join(module_dir, 'data', 'yeast_tavazoie', 'genes_yeast_tavazoie.txt'), dtype=np.str)
    return pd.DataFrame(data, index=genes)
