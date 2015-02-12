'''
Created on Feb 12, 2015

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


    def testRecoverTree_TC1(self):
        testdataTrue = "{}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = "{}"

        # act
        bt.rootnode = self.testedobj.recoverTree(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()