import numpy as np
from Pyfhel import Pyfhel

import time
from scipy import stats

from biclustlib.algorithms import ChengChurchAlgorithm
from biclustlib.algorithms import SecuredChengChurchAlgorithm
from biclustlib.algorithms import SecuredChengChurchAlgorithm1
from biclustlib.algorithms import SecuredChengChurchAlgorithm2
from biclustlib.algorithms import SecuredChengChurchAlgorithm3
from biclustlib.algorithms import SecuredChengChurchAlgorithm4
from biclustlib import models
from biclustlib.evaluation import csi
from biclustlib.evaluation import liu_wang_match_score
from biclustlib.evaluation import clustering_error
from biclustlib.evaluation import clustering_error
from biclustlib.datasets import load_yeast_tavazoie
from pandas.plotting import parallel_coordinates

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = load_yeast_tavazoie().values
num_rows, num_cols = data.shape

cca = ChengChurchAlgorithm(num_biclusters=5, msr_threshold=300.0, multiple_node_deletion_threshold=1.2)
secca = SecuredChengChurchAlgorithm(num_biclusters=5, msr_threshold=300.0, multiple_node_deletion_threshold=1.2)
type1 = SecuredChengChurchAlgorithm1(num_biclusters=5, msr_threshold=300.0, multiple_node_deletion_threshold=1.2)
type2 = SecuredChengChurchAlgorithm2(num_biclusters=5, msr_threshold=300.0, multiple_node_deletion_threshold=1.2)
type3 = SecuredChengChurchAlgorithm3(num_biclusters=5, msr_threshold=300.0, multiple_node_deletion_threshold=1.2)
type4 = SecuredChengChurchAlgorithm4(num_biclusters=5, msr_threshold=300.0, multiple_node_deletion_threshold=1.2)

secca_alog = [type1, type2, type3, type4, secca]
biclustering_ref = cca.run(data)
# biclustering_pre = type4.run(data)
csi_eval = []
ce_eval = []

for i in range(len(secca_alog)):
    print(secca_alog[i])
    biclustering_pre = secca_alog[i].run(data)
    # csi_eval.append(csi(biclustering_pre, biclustering_ref, num_rows, num_cols))
    ce_eval.append(round(clustering_error(biclustering_pre, biclustering_ref, num_rows, num_cols),5))
    print(ce_eval)

# csi_eval.append(csi(biclustering_pre, biclustering_ref, num_rows, num_cols))
# li = liu_wang_match_score(biclustering_pre, biclustering_ref)
# ce = clustering_error(biclustering_pre, biclustering_ref, num_rows, num_cols)
print(ce_eval)
# print(ce_eval)
secured_alg = ["Type1", "Type2", "Type3", "Type4", "Total"]
# ce = [type2=0.10450762829403606, type4=0.1637874871277557]
# plt.bar(secured_alg, csi_eval, color='red')
# plt.title('Comparison of SeCCA with CCA')
# plt.xlabel('Types of SeCCA')
# plt.ylabel('CSI External Evaluation Measure')
# plt.savefig('CSI_final.png')
# plt.show()

plt.bar(secured_alg, ce_eval, color='blue')
plt.title('Comparison of SeCCA with CCA')
plt.xlabel('Types of SeCCA')
plt.ylabel('CE External Evaluation Measure ')
plt.savefig('CE_final.png')
plt.show()