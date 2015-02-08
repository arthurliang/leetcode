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


    def testConnect_TC1(self):
        # arrange

        # act
        self.testedobj.connect(None)

        # assert


    def testConnect_TC2(self):
        # arrange
        testdataTrue = "{1}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRslt = "{1,#}"

        # act
        self.testedobj.connect(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ4BTnextProperty()
        self.assertEqual(expRslt, actRslt)


    def testConnect_TC3(self):
        # arrange
        testdataTrue = "{1,2,3}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRslt = "{1,#,2,3,#}"

        # act
        self.testedobj.connect(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ4BTnextProperty()
        self.assertEqual(expRslt, actRslt)


    def testConnect_TC4(self):
        # arrange
        testdataTrue = "{1,2,3,4,5,6,7}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRslt = "{1,#,2,3,#,4,5,6,7,#}"

        # act
        self.testedobj.connect(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ4BTnextProperty()
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()