"""
    SeCCA: A Python library of privacy-preserved biclustering algorithm (Cheng and Church) with Homomorphic Encryption
    Copyright (C) 2022  Shokofeh VahidianSadegh
    This file is part of SeCCA.
"""

import numpy as np

from .check import check_biclusterings

def liu_wang_match_score(predicted_biclustering, reference_biclustering):
    """Liu & Wang match score.

    Reference
    ---------
    Liu, X., & Wang, L. (2006). Computing the maximum similarity bi-clusters of gene expression data.
    Bioinformatics, 23(1), 50-56.

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
    lw_match_score : float
        Liu and Wang match score between 0.0 and 1.0.
    """
    check = check_biclusterings(predicted_biclustering, reference_biclustering)

    if isinstance(check, float):
        return check

    k = len(predicted_biclustering.biclusters)

    return sum(max((len(np.intersect1d(bp.rows, br.rows)) + len(np.intersect1d(bp.cols, br.cols))) /
        (len(np.union1d(bp.rows, br.rows)) + len(np.union1d(bp.cols, br.cols)))
        for br in reference_biclustering.biclusters)
        for bp in predicted_biclustering.biclusters) / k
