import numbers
from numbers import Integral

class VerifiedSet(set):
    """A subclass of set which ore only valid for certain values"""

    def __init__(self, iterable=()):
        for item in iterable:
            self._verify(item)
        super().__init__(iterable)

    def _verify(self,value):
        raise NotImplementedError()

    def update(self,value):
        self._verify(value)
        super().update(value)

    def add(self,value):
        self._verify(value)
        super().add(value)

    def symmetric_difference_update(self,value):
        self._verify(value)
        super().symmetric_difference_update(value)

    def union(self,value):
        return type(self)(super().union(self , value))

    def intersection(self,value):
        return type(self)(super().intersection(self , value))

    def difference(self,value):
        return type(self)(super().difference(self , value))

    def symmetric_difference(self,value):
        return type(self)(super().symmetric_difference(self , value))

    def copy(self):
        return type(self)(super().copy())


class IntSet(VerifiedSet):

    def _verify(self,value):
        if hasattr(value,"__iter__"):
            for i in value:
                if not isinstance(i,numbers.Integral):
                    raise TypeError("IntSet expected an Integer got a",type(value),__name__)
        else:
            if not isinstance(value, numbers.Integral):
                raise TypeError("IntSet expected an Integer got a", type(value), __name__)
