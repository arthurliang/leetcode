'''
Created on Feb 8, 2015

@author: Arthur
'''
import unittest
import Solution
from utility import BinTree


class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testBuildTree_TC1(self):
        # arrange
        expRslt = None
        preorder = []
        inorder = []

        # act
        actRslt = self.testedobj.buildTree(preorder, inorder)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testBuildTree_TC2(self):
        # arrange
        expRslt = "{1}"
        preorder = [1]
        inorder = [1]

        # act
        actRslt = self.testedobj.buildTree(preorder, inorder)

        # assert
        bt = BinTree.BinTree()
        bt.rootnode = actRslt
        self.assertEqual(expRslt, bt.SerializationOnOJ())


    def testBuildTree_TC3(self):
        # arrange
        expRslt = "{1,2}"
        preorder = [1, 2]
        inorder = [2, 1]

        # act
        actRslt = self.testedobj.buildTree(preorder, inorder)

        # assert
        bt = BinTree.BinTree()
        bt.rootnode = actRslt
        self.assertEqual(expRslt, bt.SerializationOnOJ())


    def testBuildTree_TC5(self):
        # arrange
        expRslt = "{1,#,2}"
        preorder = [1, 2]
        inorder = [1, 2]

        # act
        actRslt = self.testedobj.buildTree(preorder, inorder)

        # assert
        bt = BinTree.BinTree()
        bt.rootnode = actRslt
        self.assertEqual(expRslt, bt.SerializationOnOJ())


    def testBuildTree_TC6(self):
        # arrange
        expRslt = "{1,2,3}"
        preorder = [1,2,3]
        inorder = [2,1,3]

        # act
        actRslt = self.testedobj.buildTree(preorder, inorder)

        # assert
        bt = BinTree.BinTree()
        bt.rootnode = actRslt
        self.assertEqual(expRslt, bt.SerializationOnOJ())


    def testBuildTree_TC7(self):
        # arrange
        expRslt = "{1,2,#,3}"
        preorder = [1,2,3]
        inorder = [3,2,1]

        # act
        actRslt = self.testedobj.buildTree(preorder, inorder)

        # assert
        bt = BinTree.BinTree()
        bt.rootnode = actRslt
        self.assertEqual(expRslt, bt.SerializationOnOJ())


    def testBuildTree_TC8(self):
        # arrange
        expRslt = "{1,#,2,#,3}"
        preorder = [1,2,3]
        inorder = [1,2,3]

        # act
        actRslt = self.testedobj.buildTree(preorder, inorder)

        # assert
        bt = BinTree.BinTree()
        bt.rootnode = actRslt
        self.assertEqual(expRslt, bt.SerializationOnOJ())


    def testBuildTree_TC9(self):
        # arrange
        expRslt = "{1,#,2,3}"
        preorder = [1,2,3]
        inorder = [1,3,2]

        # act
        actRslt = self.testedobj.buildTree(preorder, inorder)

        # assert
        bt = BinTree.BinTree()
        bt.rootnode = actRslt
        self.assertEqual(expRslt, bt.SerializationOnOJ())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()