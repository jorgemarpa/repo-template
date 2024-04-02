"""
This is an example Python class to show how docstrings, pytest, and black works
"""

import numpy as np

__all__ = ["MyClass"]


class MyClass(object):
    """
    This is my example class and it does things in order
    """

    def __init__(self, order: bool = True):
        """
        Parameters
        ----------
        order : bool, optional
            Set if things are done in order or not, by default True
        """
        self.order = order
        self.memory = None

    def sum(self, a: float = 1, b: int = 2) -> float:
        """
        Sum two values

        Parameters
        ----------
        a : float, optional
            first value to sum, by default 1
        b : int, optional
            second value to sum, by default 2

        Returns
        -------
        result : float
            result of sum
        """
        if self.order:
            result = np.sum([a, b])
        return result

    def multiply(self, a: float = 1, b: float = 2) -> float:
        """
        Multiply two values and return result

        Parameters
        ----------
        a : float, optional
            First value, by default 1
        b : float, optional
            Second value, by default 2

        Returns
        -------
        result : float
            result of multiplication
        """
        if self.order:
            result = a * b
        return result
