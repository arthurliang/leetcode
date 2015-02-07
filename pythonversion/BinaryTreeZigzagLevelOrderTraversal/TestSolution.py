'''
Created on Feb 7, 2015

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


    def testZigzagLevelOrder_TC1(self):
        # arrange
        expRst = []

        # act
        actRslt = self.testedobj.zigzagLevelOrder(None)

        # assert
        self.assertEqual(expRst, actRslt)


    def testZigzagLevelOrder_TC2(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [[1]]

        # act
        actRslt = self.testedobj.zigzagLevelOrder(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testZigzagLevelOrder_TC3(self):
        # arrange
        testdataTrue = "{1,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [[1],
                  [2]
                  ]

        # act
        actRslt = self.testedobj.zigzagLevelOrder(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testZigzagLevelOrder_TC4(self):
        # arrange
        testdataTrue = "{1,#,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [[1],
                  [2]
                  ]

        # act
        actRslt = self.testedobj.zigzagLevelOrder(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testZigzagLevelOrder_TC5(self):
        # arrange
        testdataTrue = "{1,3,2}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [[1],
                  [2,3]
                  ]

        # act
        actRslt = self.testedobj.zigzagLevelOrder(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testZigzagLevelOrder_TC6(self):
        # arrange
        testdataTrue = "{3,9,20,#,#,15,7}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [[3],
                  [20,9],
                  [15,7]
                  ]

        # act
        actRslt = self.testedobj.zigzagLevelOrder(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testZigzagLevelOrder_TC7(self):
        # arrange
        testdataTrue = "{1,2,3,4,#,#,5}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [[1],
                  [3,2],
                  [4,5]
                  ]

        # act
        actRslt = self.testedobj.zigzagLevelOrder(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)


    def testZigzagLevelOrder_TC8(self):
        # arrange
        testdataTrue = "{0,2,4,1,#,3,-1,5,1,#,6,#,8}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [[0],
                  [4,2],
                  [1,3,-1],
                  [8,6,1,5]]


        # act
        actRslt = self.testedobj.zigzagLevelOrder(bt.rootnode)

        # assert
        self.assertEqual(expRst, actRslt)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()