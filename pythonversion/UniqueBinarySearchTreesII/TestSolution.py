'''
Created on Feb 9, 2015

@author: Arthur
'''
import unittest
import Solution
from utility.BinTree import BinTree


class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testGenerateTrees_TC1(self):
        # arrange
        n = 0
        expListRslt = [None]

        bt = BinTree()
        expRslt = [bt.SerializationOnOJbyPara(x) for x in expListRslt]

        # act
        actLsitRslt = self.testedobj.generateTrees(n)

        # assert
        actRslt = [bt.SerializationOnOJbyPara(x) for x in actLsitRslt]
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()