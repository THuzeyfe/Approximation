# Any changes to the distributions library should be reinstalled with
#  pip install --upgrade .

# For running unit tests, use
# /usr/bin/python -m unittest test

import unittest

import math
from scipy.stats import lognorm
from Approximation.lognormalAproximations import FentonWilkinson, SchwartzYeh_tabular
#from Approximation.Approximation import FentonWilkinson

class TestLognormalApproximations(unittest.TestCase):
    def setUp(self):
        self.dist1 = lognorm(s=0.3,loc=0,scale=math.exp(1))
        self.dist2 = lognorm(s=0.4,loc=0,scale=math.exp(1.2))

    def test_Fenton_Wilkinson(self): #print(results.mean(), results.var(), results.kwds['loc'])
        FW = FentonWilkinson(self.dist1, self.dist2)
        self.assertEqual(FW.mean(),  6.440038249221049, "calculated mean is not expected")
        self.assertEqual(FW.var(),  3.0058960238266414, "calculated variance is not expected")
        self.assertEqual(FW.support()[0],  0, "calculated loc is not expected")

    def test_Schwartz_Yeh_tabular(self): #print(results.mean(), results.var(), results.kwds['loc'])
        SY = SchwartzYeh_tabular(self.dist1, self.dist2)
        self.assertEqual(SY.mean(),  4.642702806163277, "calculated mean is not expected")
        self.assertEqual(SY.var(),  20.59328203150837, "calculated variance is not expected")
        self.assertEqual(SY.support()[0],  0, "calculated loc is not expected")

    def test_commutativity(self):
        self.assertEqual(FentonWilkinson(self.dist1, self.dist2).mean(), FentonWilkinson(self.dist2, self.dist1).mean(),"commutativity feature is not satisfied for Fenton Approximation")
        self.assertEqual(SchwartzYeh_tabular(self.dist1, self.dist2).mean(), SchwartzYeh_tabular(self.dist2, self.dist1).mean(),"commutativity feature is not satisfied for Schwartz-Yeh" )
        self.assertEqual(FentonWilkinson(self.dist1, self.dist2).var(), FentonWilkinson(self.dist2, self.dist1).var(),"commutativity feature is not satisfied for Fenton Approximation")
        self.assertEqual(SchwartzYeh_tabular(self.dist1, self.dist2).var(), SchwartzYeh_tabular(self.dist2, self.dist1).var(),"commutativity feature is not satisfied for Schwartz-Yeh" )
        self.assertEqual(FentonWilkinson(self.dist1, self.dist2).support()[0], FentonWilkinson(self.dist2, self.dist1).support()[0],"commutativity feature is not satisfied for Fenton Approximation")
        self.assertEqual(SchwartzYeh_tabular(self.dist1, self.dist2).support()[0], SchwartzYeh_tabular(self.dist2, self.dist1).support()[0],"commutativity feature is not satisfied for Schwartz-Yeh" )
        
if __name__ == '__main__':
    unittest.main()