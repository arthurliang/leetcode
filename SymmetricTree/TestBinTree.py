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
        self.testBinTreeIsNullAfterConstruct()


    def testBinTreeDeserializationOnOJforParameterVerifyWithWrongSurfix(self):
        # arrange
        srlztn = "{#"

        # act
        rulst = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(rulst, False)
        self.testBinTreeIsNullAfterConstruct()


    def testBinTreeDeserializationOnOJforNullTreeWithSharp(self):
        # arrange
        srlztn = "{#}"

        # act
        rulst = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(rulst, True)
        self.assertNotEqual(self.testedobj.rootnode, None)
        self.assertEqual(self.testedobj.rootnode.val, None)
        self.assertEqual(self.testedobj.rootnode.left, None)
        self.assertEqual(self.testedobj.rootnode.right, None)


    def testBinTreeDeserializationOnOJforFullcase(self):
        # arrange
        srlztn = "{1,2,3,#,#,4,#,#,5}"

        # act
        rulst = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(rulst, True)

        self.assertNotEqual(self.testedobj.rootnode, None)
        self.assertEqual(self.testedobj.rootnode.val, '1')

        self.assertNotEqual(self.testedobj.rootnode.left, None)
        self.assertEqual(self.testedobj.rootnode.left.val, '2')

        self.assertNotEqual(self.testedobj.rootnode.right, None)
        self.assertEqual(self.testedobj.rootnode.right.val, '3')

        self.assertEqual(self.testedobj.rootnode.left.left.val, None)
        self.assertEqual(self.testedobj.rootnode.left.left.left, None)
        self.assertEqual(self.testedobj.rootnode.left.left.right, None)

        self.assertEqual(self.testedobj.rootnode.left.right.val, None)
        self.assertEqual(self.testedobj.rootnode.left.right.left, None)
        self.assertEqual(self.testedobj.rootnode.left.right.right, None)

        self.assertNotEqual(self.testedobj.rootnode.right.left, None)
        self.assertEqual(self.testedobj.rootnode.right.left.val, '4')

        self.assertEqual(self.testedobj.rootnode.right.right.val, None)
        self.assertEqual(self.testedobj.rootnode.right.right.left, None)
        self.assertEqual(self.testedobj.rootnode.right.right.right, None)

        self.assertEqual(self.testedobj.rootnode.right.left.left.val, None)
        self.assertEqual(self.testedobj.rootnode.right.left.left.left, None)
        self.assertEqual(self.testedobj.rootnode.right.left.left.right, None)

        self.assertNotEqual(self.testedobj.rootnode.right.left.right, None)
        self.assertEqual(self.testedobj.rootnode.right.left.right.val, '5')

        self.assertEqual(self.testedobj.rootnode.right.left.right.left.val, None)
        self.assertEqual(self.testedobj.rootnode.right.left.right.left.left, None)
        self.assertEqual(self.testedobj.rootnode.right.left.right.left.right, None)

        self.assertEqual(self.testedobj.rootnode.right.left.right.right.val, None)
        self.assertEqual(self.testedobj.rootnode.right.left.right.right.left, None)
        self.assertEqual(self.testedobj.rootnode.right.left.right.right.right, None)


    def testBinTreeSerializationOnOJforNullTree(self):
        # arrange
        expSrlztn = "{#}"
        rulst = self.testedobj.DeserializationOnOJ(expSrlztn)
        self.assertEqual(rulst, True)

        # act
        actSrlztn = self.testedobj.SerializationOnOJ()

        # assert
        self.assertEqual(expSrlztn, actSrlztn)


    def testBinTreeSerializationOnOJforFullcase(self):
        # arrange
        expSrlztn = "{1,2,3,#,#,4,#,#,5}"
        rulst = self.testedobj.DeserializationOnOJ(expSrlztn)
        self.assertEqual(rulst, True)

        # act
        actSrlztn = self.testedobj.SerializationOnOJ()

        # assert
        self.assertEqual(expSrlztn, actSrlztn)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()