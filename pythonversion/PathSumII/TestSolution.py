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


    def testPathSum_TC1(self):
        # arrange
        sum = 0
        expRslt = []

        # act
        actRslt = self.testedobj.pathSum(None, sum)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testPathSum_TC2(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        sum = 1

        expRslt = [[1]]

        # act
        actRslt = self.testedobj.pathSum(bt.rootnode, sum)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testPathSum_TC3(self):
        # arrange
        testdataTrue = "{1,2,2}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        sum = 3

        expRslt = [[1,2],[1,2]]

        # act
        actRslt = self.testedobj.pathSum(bt.rootnode, sum)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testPathSum_TC4(self):
        # arrange
        testdataTrue = "{1,2,1,3,#,1,2,#,#,3,#,#,2}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        sum = 6

        expRslt = [[1,2,3],[1,1,1,3],[1,1,2,2]]

        # act
        actRslt = self.testedobj.pathSum(bt.rootnode, sum)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()