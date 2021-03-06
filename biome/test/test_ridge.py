"""
unit test module for testing ridge regression
use synthetic data to test
"""


import unittest
from sklearn.datasets import make_classification

import biome


class Test_ridge(unittest.TestCase):
    """
    unit test for knn_regression module, this class is inhered child class of
    unittest. unittest.TestCase is parent class.
    """
    def test_1(self):
        """smoke test: argument rule is inherited from unittest, no return
        value"""
        """dependent variable contain 2 class"""
        X, y = make_classification(n_samples=10000, n_informative=4,
                                   n_features=20, n_classes=2)
        model = biome.Ridge_regress(X, y)
        self.assertTrue(model)

    def test_2(self):
        """smoke test: argument rule is inherited from unittest, no return
        value"""
        """dependent variable contain 3 class"""
        X, y = make_classification(n_samples=10000, n_informative=4,
                                   n_features=50, n_classes=3)
        model = biome.Ridge_regress(X, y)
        self.assertTrue(model)

    def test_3(self):
        """smoke test: argument rule is inherited from unittest, no return
        value"""
        """dependent variable contain 4 class"""
        X, y = make_classification(n_samples=10000, n_informative=4,
                                   n_features=60, n_classes=4)
        result = biome.Ridge_regress(X, y)
        self.assertTrue(result)


suite = unittest.TestLoader().loadTestsFromTestCase(Test_ridge)
_ = unittest.TextTestRunner().run(suite)
