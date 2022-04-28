"""
     SeCCA: A Python library of privacy-preserved biclustering algorithm (Cheng and Church) with Homomorphic Encryption
    Copyright (C) 2022  Shokofeh VahidianSadegh
    This file is part of SeCCA.
"""

import numpy as np

from math import sqrt
from .check import check_biclusterings

def prelic_relevance(predicted_biclustering, reference_biclustering):
    """The overall relevance match score defined in the supplementary material of Prelic et al. (2006).
    This score reflects how well the predicted biclusters represent the reference biclusters in both dimensions
    (rows and columns). This measure lies in the interval [0, 1], where values close to 1 indicate better
    biclustering solutions.

    Reference
    ---------
    Prelic, A., Bleuler, S., Zimmermann, P., Wille, A., Buhlmann, P., Gruissem, W., Hennig, L., Thiele, L. &
    Zitzler, E. (2006). A systematic comparison and evaluation of biclustering methods for gene expression data.
    Bioinformatics, 22(9), 1122-1129.

    Horta, D., & Campello, R. J. G. B. (2014). Similarity measures for comparing biclusterings.
    IEEE/ACM Transactions on Computational Biology and Bioinformatics, 11(5), 942-954.

    Parameters
    ----------
    predicted_biclustering : biclustlib.model.Biclustering
        Predicted biclustering solution.

    reference_biclustering : biclustlib.model.Biclustering
        Reference biclustering solution.

    Returns
    -------
    prel : float
        Similarity score between 0.0 and 1.0.
    """
    check = check_biclusterings(predicted_biclustering, reference_biclustering)

    if isinstance(check, float):
        return check

    row_score = _match_score(predicted_biclustering, reference_biclustering, 'rows')
    col_score = _match_score(predicted_biclustering, reference_biclustering, 'cols')

    return sqrt(row_score * col_score)

def prelic_recovery(predicted_biclustering, reference_biclustering):
    """The overall recovery match score defined in the supplementary material of Prelic et al. (2006).
    This score reflects how well each of the reference biclusters is recovered by the predicted biclustering.
    This measure lies in the interval [0, 1], where values close to 1 indicate better biclustering solutions.

    Reference
    ---------
    Prelic, A., Bleuler, S., Zimmermann, P., Wille, A., Buhlmann, P., Gruissem, W., Hennig, L., Thiele, L. &
    Zitzler, E. (2006). A systematic comparison and evaluation of biclustering methods for gene expression data.
    Bioinformatics, 22(9), 1122-1129.

    Horta, D., & Campello, R. J. G. B. (2014). Similarity measures for comparing biclusterings.
    IEEE/ACM Transactions on Computational Biology and Bioinformatics, 11(5), 942-954.

    Parameters
    ----------
    predicted_biclustering : biclustlib.model.Biclustering
        Predicted biclustering solution.

    reference_biclustering : biclustlib.model.Biclustering
        Reference biclustering solution.

    Returns
    -------
    prec : float
        Similarity score between 0.0 and 1.0.
    """
    check = check_biclusterings(predicted_biclustering, reference_biclustering)

    if isinstance(check, float):
        return check

    return prelic_relevance(reference_biclustering, predicted_biclustering)

def _match_score(predicted_biclustering, reference_biclustering, bicluster_attr):
    k = len(predicted_biclustering.biclusters)
    return sum(max(len(np.intersect1d(getattr(bp, bicluster_attr), getattr(bt, bicluster_attr))) /
        len(np.union1d(getattr(bp, bicluster_attr), getattr(bt, bicluster_attr)))
        for bt in reference_biclustering.biclusters)
        for bp in predicted_biclustering.biclusters) / k
