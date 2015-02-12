'''
Created on Feb 12, 2015

@author: Arthur
'''
import unittest
from Solution import BSTIterator
from utility import BinTree


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testBSTIterator_TC1(self):
        # arrange
        testdataTrue = "{}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = []

        # act
        i, actRslt = BSTIterator(bt.rootnode), []
        while i.hasNext():
            actRslt.append(i.next())

        # assert
        self.assertEqual(expRst, actRslt)


    def testBSTIterator_TC2(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [1]

        # act
        i, actRslt = BSTIterator(bt.rootnode), []
        while i.hasNext():
            actRslt.append(i.next())

        # assert
        self.assertEqual(expRst, actRslt)


    def testBSTIterator_TC3(self):
        # arrange
        testdataTrue = "{2,1,3}"
        bt = BinTree.BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRst = [1,2,3]

        # act
        i, actRslt = BSTIterator(bt.rootnode), []
        while i.hasNext():
            actRslt.append(i.next())

        # assert
        self.assertEqual(expRst, actRslt)




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()