"""
    SeCCA: A Python library of privacy-preserved biclustering algorithm (Cheng and Church) with Homomorphic Encryption

    Copyright (C) 2022  Shokofeh VahidianSadegh

    This file is part of SeCCA.

"""

from abc import ABCMeta, abstractmethod

class BaseBiclusteringAlgorithm(object, metaclass=ABCMeta):
    """A class that defines the skeleton of a biclustering algorithm implementation."""

    @abstractmethod
    def run(self, data):
        """Method needed to run a biclustering algorithm."""
        pass

    @abstractmethod
    def _validate_parameters(self):
        """Method to validate the input parameters of a biclustering algorithm, if necessary."""
        pass
