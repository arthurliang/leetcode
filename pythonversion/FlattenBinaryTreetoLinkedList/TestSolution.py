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


    def testFlatten_TC2(self):
        # arrange
        testdataTrue = "{1,2}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRslt = "{1,#,2}"

        # act
        self.testedobj.flatten(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testFlatten_TC3(self):
        # arrange
        testdataTrue = "{1,#,2}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRslt = "{1,#,2}"

        # act
        self.testedobj.flatten(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testFlatten_TC4(self):
        # arrange
        testdataTrue = "{1,#,2,#,3}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRslt = "{1,#,2,#,3}"

        # act
        self.testedobj.flatten(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testFlatten_TC5(self):
        # arrange
        testdataTrue = "{1,2,3}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRslt = "{1,#,2,#,3}"

        # act
        self.testedobj.flatten(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testFlatten_TC6(self):
        # arrange
        testdataTrue = "{1,2,#,3}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRslt = "{1,#,2,#,3}"

        # act
        self.testedobj.flatten(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testFlatten_TC7(self):
        # arrange
        testdataTrue = "{2,1,4,#,#,3}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRslt = "{2,#,1,#,4,#,3}"

        # act
        self.testedobj.flatten(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testFlatten_TC8(self):
        # arrange
        testdataTrue = "{1,#,2,3}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)

        expRslt = "{1,#,2,#,3}"

        # act
        self.testedobj.flatten(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()