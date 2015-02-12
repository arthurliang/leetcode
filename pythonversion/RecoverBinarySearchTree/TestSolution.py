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


    def testRecoverTree_TC2(self):
        testdataTrue = "{1}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = "{1}"

        # act
        bt.rootnode = self.testedobj.recoverTree(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testRecoverTree_TC3(self):
        testdataTrue = "{0,1}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = "{1,0}"

        # act
        bt.rootnode = self.testedobj.recoverTree(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testRecoverTree_TC4(self):
        testdataTrue = "{1,#,0}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = "{0,#,1}"

        # act
        bt.rootnode = self.testedobj.recoverTree(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testRecoverTree_TC5(self):
        testdataTrue = "{0,1,2}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = "{1,0,2}"

        # act
        bt.rootnode = self.testedobj.recoverTree(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testRecoverTree_TC6(self):
        testdataTrue = "{2,0,1}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = "{1,0,2}"

        # act
        bt.rootnode = self.testedobj.recoverTree(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testRecoverTree_TC7(self):
        testdataTrue = "{1,2,0}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = "{1,0,2}"

        # act
        bt.rootnode = self.testedobj.recoverTree(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testRecoverTree_TC8(self):
        testdataTrue = "{20,15,25,10,22,17}"
        bt = BinTree()
        bt.DeserializationOnOJ(testdataTrue)
        expRslt = "{20,15,25,10,17,22}"

        # act
        bt.rootnode = self.testedobj.recoverTree(bt.rootnode)

        # assert
        actRslt = bt.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()