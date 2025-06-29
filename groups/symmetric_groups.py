from example_code.groups import Group , Element
import numpy as np


class SymmetricGroup(Group):
    """The group whose members are all the permutations of n symbols"""
    symbol = "S"

    def _validate(self,value):
        list_comparison = np.array([i for i in range(self.n)])
        if not sorted(list_comparison) == sorted(np.array([i for i in range(self.n)])):
            raise ValueError("Element must be a permutation of",self.n,"objects")

    def operation(self , a , b):
        return a[b]

