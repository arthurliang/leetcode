'''
Created on Dec 14, 2014

@author: Arthur
'''
import unittest
import Solution
import BinTree

class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testIsBalancedWhenRootIsNone(self):
        # arrange

        # act
        actRslt = self.testedobj.isBalanced(None)

        # assert
        self.assertEqual(True, actRslt)


    def testIsBalancedWhenRootIsNotNoneAndLeftRightDepthNotLessThanOne(self):
        # arrange
        testdataTrue = "{1,2,#,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.isBalanced(bt.rootnode)

        # assert
        self.assertEqual(False, actRslt)


    def testIsBalancedWhenRootIsNotNoneAndLeftRightTreeIsBothBalancedAndLeftRightDepthLessThanOne(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.isBalanced(bt.rootnode)

        # assert
        self.assertEqual(True, actRslt)


    def testIsBalancedWhenRootIsNotNoneAndLeftRightTreeIsBothBalancedButLeftRightTreeDepthNotLessThanOne(self):
        # arrange
        testdataTrue = "{1,2,4,3,5,#,#,6}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.isBalanced(bt.rootnode)

        # assert
        self.assertEqual(False, actRslt)


    def testIsBalancedWhenRootIsNotNoneAndOneOfLeftRightTreeIsNotBalanced(self):
        # arrange
        testdataTrue = "{1,2,4,3,5,#,#,6,#,#,#,7}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        # act
        actRslt = self.testedobj.isBalanced(bt.rootnode)

        # assert
        self.assertEqual(False, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()