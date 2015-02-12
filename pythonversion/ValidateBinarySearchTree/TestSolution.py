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


    def testIsValidBST_TC1(self):
        # arrange
        expRslt = True

        # act
        actRslt = self.testedobj.isValidBST(None)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC2(self):
        testdataTrue = "{1}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = True

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC3(self):
        testdataTrue = "{1,2}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = False

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC4(self):
        testdataTrue = "{3,1,#,2}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = False

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC5(self):
        testdataTrue = "{2,1}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = True

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC6(self):
        testdataTrue = "{3,2,#,1}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = True

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC7(self):
        testdataTrue = "{2,#,1}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = False

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC8(self):
        testdataTrue = "{2,#,3,#,0}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = False

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()