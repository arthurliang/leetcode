'''
Created on Feb 8, 2015

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


    def testFlatten_TC1(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRslt = "{1}"

        # act
        self.testedobj.flatten(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()