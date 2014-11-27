'''
Created on Nov 16, 2014

@author: Arthur
'''
import unittest
from BinTree import *

class Test(unittest.TestCase):

    def setUp(self):
        self.testedobj = BinTree()
        pass


    def tearDown(self):
        pass


    def testBinTreeIsNullAfterConstruct(self):
        self.assertEqual(self.testedobj.rootnode, None)
        pass

    def testBinTreeDeserializationOnOJforParameterVerifyWithWrongPrefix(self):
        # arrange
        srlztn = "#"

        # act
        rulst = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(rulst, False)
        self.assertEqual(self.testedobj.rootnode, None)

    def testBinTreeDeserializationOnOJforParameterVerifyWithWrongSurfix(self):
        # arrange
        srlztn = "{#"

        # act
        rulst = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(rulst, False)
        self.assertEqual(self.testedobj.rootnode, None)

    def testBinTreeDeserializationOnOJforNullTree(self):
        # arrange
        srlztn = "{#}"

        # act
        self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(self.testedobj.rootnode, None)

    def testBinTreeDeserializationOnOJforFullcase(self):
        # arrange
        srlztn = "{1,2,3,#,#,4,#,#,5}"

        # act
        self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertNotEqual(self.testedobj.rootnode, None)
        self.assertEqual(self.testedobj.rootnode.val, 1)
        self.assertEqual(self.testedobj.rootnode.left, None)
        self.assertEqual(self.testedobj.rootnode.right, None)




if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()