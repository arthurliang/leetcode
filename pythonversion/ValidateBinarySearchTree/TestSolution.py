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
        testdataTrue = "{2,#,1,#,3}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = False

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC9(self):
        testdataTrue = "{1,#,3,#,2}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = False

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC10(self):
        testdataTrue = "{2,1,#,0,3}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = False

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC11(self):
        testdataTrue = "{2,#,3,1}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = False

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC12(self):
        testdataTrue = "{4,2,6,1,3,5,7}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = True

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC13(self):
        testdataTrue = "{10,5,15,#,#,6,20}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = False

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC14(self):
        testdataTrue = "{1,1}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = False

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC15(self):
        testdataTrue = "{1,#,1}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = False

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC16(self):
        testdataTrue = "{3,2,5,#,3,3,6}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = False

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC17(self):
        testdataTrue = "{87,84,94,-82,#,#,#,70}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = False

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC18(self):
        testdataTrue = "{87,84,94,#,#,#,-82}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = False

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC19(self):
        testdataTrue = "{5,14,#,1}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = False

        # act
        actRslt = self.testedobj.isValidBST(bt.rootnode)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValidBST_TC20(self):
        testdataTrue = "{3,1,5,0,2,4,6,#,#,#,3}"
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