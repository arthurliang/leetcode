'''
Created on Nov 16, 2014

@author: Arthur
'''
import unittest
import BinTree

class Test(unittest.TestCase):

    def setUp(self):
        self.testedobj = BinTree.BinTree()
        pass


    def tearDown(self):
        self.testedobj.rootnode = None
        pass


    def testBinTreeIsNullAfterConstruct(self):
        self.assertEqual(self.testedobj.rootnode, None)


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


    def testBinTreeDeserializationOnOJforParameterVerifyWithOnlySharpAtTheEnd(self):
        # arrange
        srlztn = "{#}"

        # act
        rulst = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(rulst, False)
        self.testBinTreeIsNullAfterConstruct()


    def testBinTreeDeserializationOnOJforParameterVerifyWithSharpAtTheEnd(self):
        # arrange
        srlztn = "{1,#}"

        # act
        rulst = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(rulst, False)
        self.testBinTreeIsNullAfterConstruct()


    def testBinTreeDeserializationOnOJfor1TreeNodeWithEmptyStr(self):
        # arrange
        srlztn = "{}"

        # act
        rulst = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(rulst, True)
        self.assertEqual(self.testedobj.rootnode, None)


    def testBinTreeDeserializationOnOJforSimpleCase(self):
        # arrange
        srlztn = "{1,2}"

        # act
        rulst = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(rulst, True)

        self.assertNotEqual(self.testedobj.rootnode, None)
        self.assertEqual(self.testedobj.rootnode.val, '1')

        self.assertNotEqual(self.testedobj.rootnode.left, None)
        self.assertEqual(self.testedobj.rootnode.left.val, '2')
        self.assertEqual(self.testedobj.rootnode.left.left, None)
        self.assertEqual(self.testedobj.rootnode.left.right, None)

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
        self.assertEqual(self.testedobj.rootnode.left.left, None)
        self.assertEqual(self.testedobj.rootnode.left.right, None)

        self.assertNotEqual(self.testedobj.rootnode.right, None)
        self.assertEqual(self.testedobj.rootnode.right.val, '3')
        self.assertEqual(self.testedobj.rootnode.right.right, None)

        self.assertNotEqual(self.testedobj.rootnode.right.left, None)
        self.assertEqual(self.testedobj.rootnode.right.left.val, '4')
        self.assertEqual(self.testedobj.rootnode.right.left.left, None)

        self.assertNotEqual(self.testedobj.rootnode.right.left.right, None)
        self.assertEqual(self.testedobj.rootnode.right.left.right.val, '5')
        self.assertEqual(self.testedobj.rootnode.right.left.right.left, None)
        self.assertEqual(self.testedobj.rootnode.right.left.right.right, None)


    def testBinTreeSerializationOnOJforNullTree(self):
        # arrange
        expSrlztn = "{}"

        # act
        actSrlztn = self.testedobj.SerializationOnOJ()

        # assert
        self.assertEqual(expSrlztn, actSrlztn)


    def testBinTreeSerializationOnOJforSimpleCase(self):
        # arrange
        expSrlztn = "{1,2}"
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