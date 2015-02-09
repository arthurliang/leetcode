'''
Created on Nov 16, 2014

@author: Arthur
'''
import unittest
import BinTree

class Test(unittest.TestCase):

    def setUp(self):
        self.testedobj = BinTree.BinTree()
        self.testedobjbst = BinTree.BinSearchTree()
        self.bst = BinTree.BinTree()
        pass


    def tearDown(self):
        self.testedobj = None
        self.testedobjbst = None
        self.bst = None
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


    def testBinTreeDeserializationOnOJfor0TreeNodeWithEmptyStr(self):
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
        self.assertEqual(self.testedobj.rootnode.val, 1)

        self.assertNotEqual(self.testedobj.rootnode.left, None)
        self.assertEqual(self.testedobj.rootnode.left.val, 2)
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
        self.assertEqual(self.testedobj.rootnode.val, 1)

        self.assertNotEqual(self.testedobj.rootnode.left, None)
        self.assertEqual(self.testedobj.rootnode.left.val, 2)
        self.assertEqual(self.testedobj.rootnode.left.left, None)
        self.assertEqual(self.testedobj.rootnode.left.right, None)

        self.assertNotEqual(self.testedobj.rootnode.right, None)
        self.assertEqual(self.testedobj.rootnode.right.val, 3)
        self.assertEqual(self.testedobj.rootnode.right.right, None)

        self.assertNotEqual(self.testedobj.rootnode.right.left, None)
        self.assertEqual(self.testedobj.rootnode.right.left.val, 4)
        self.assertEqual(self.testedobj.rootnode.right.left.left, None)

        self.assertNotEqual(self.testedobj.rootnode.right.left.right, None)
        self.assertEqual(self.testedobj.rootnode.right.left.right.val, 5)
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


    def testSerializationOnOJ4BTnextPropertyforNullTree(self):
        # arrange
        expSrlztn = "{}"

        # act
        actSrlztn = self.testedobj.SerializationOnOJ4BTnextProperty()

        # assert
        self.assertEqual(expSrlztn, actSrlztn)


    def testSerializationOnOJ4BTnextPropertyfor1Level(self):
        # arrange
        bintree = "{1}"
        rulst = self.testedobj.DeserializationOnOJ(bintree)
        self.assertEqual(rulst, True)

        expSrlztn = "{1,#}"

        # act
        actSrlztn = self.testedobj.SerializationOnOJ4BTnextProperty()

        # assert
        self.assertEqual(expSrlztn, actSrlztn)


    def testSerializationOnOJ4BTnextPropertyfor2Level_TC1(self):
        # arrange
        bintree = "{1,2,3}"
        rulst = self.testedobj.DeserializationOnOJ(bintree)
        self.assertEqual(rulst, True)
        self.testedobj.rootnode.left.next = self.testedobj.rootnode.right

        expSrlztn = "{1,#,2,3,#}"

        # act
        actSrlztn = self.testedobj.SerializationOnOJ4BTnextProperty()

        # assert
        self.assertEqual(expSrlztn, actSrlztn)


    def testSerializationOnOJ4BTnextPropertyfor3Level_TC1(self):
        # arrange
        bintree = "{1,2,3,4,5,6,7}"
        rulst = self.testedobj.DeserializationOnOJ(bintree)
        self.assertEqual(rulst, True)

        self.testedobj.rootnode.left.next = self.testedobj.rootnode.right

        self.testedobj.rootnode.left.left.next = self.testedobj.rootnode.left.right
        self.testedobj.rootnode.left.right.next = self.testedobj.rootnode.right.left
        self.testedobj.rootnode.right.left.next = self.testedobj.rootnode.right.right

        expSrlztn = "{1,#,2,3,#,4,5,6,7,#}"

        # act
        actSrlztn = self.testedobj.SerializationOnOJ4BTnextProperty()

        # assert
        self.assertEqual(expSrlztn, actSrlztn)


    def testSerializationOnOJ4BTnextPropertyfor2Level_TC2(self):
        # arrange
        bintree = "{1,2}"
        rulst = self.testedobj.DeserializationOnOJ(bintree)
        self.assertEqual(rulst, True)

        expSrlztn = "{1,#,2,#}"

        # act
        actSrlztn = self.testedobj.SerializationOnOJ4BTnextProperty()

        # assert
        self.assertEqual(expSrlztn, actSrlztn)


    def testSerializationOnOJ4BTnextPropertyfor2Level_TC3(self):
        # arrange
        bintree = "{1,#,3}"
        rulst = self.testedobj.DeserializationOnOJ(bintree)
        self.assertEqual(rulst, True)

        expSrlztn = "{1,#,3,#}"

        # act
        actSrlztn = self.testedobj.SerializationOnOJ4BTnextProperty()

        # assert
        self.assertEqual(expSrlztn, actSrlztn)


    def testSerializationOnOJ4BTnextPropertyfor3Level_TC2(self):
        # arrange
        bintree = "{1,2,#,3}"
        rulst = self.testedobj.DeserializationOnOJ(bintree)
        self.assertEqual(rulst, True)

        expSrlztn = "{1,#,2,#,3,#}"

        # act
        actSrlztn = self.testedobj.SerializationOnOJ4BTnextProperty()

        # assert
        self.assertEqual(expSrlztn, actSrlztn)


    def testSerializationOnOJ4BTnextPropertyfor3Level_TC3(self):
        # arrange
        bintree = "{1,#,2,#,3}"
        rulst = self.testedobj.DeserializationOnOJ(bintree)
        self.assertEqual(rulst, True)

        expSrlztn = "{1,#,2,#,3,#}"

        # act
        actSrlztn = self.testedobj.SerializationOnOJ4BTnextProperty()

        # assert
        self.assertEqual(expSrlztn, actSrlztn)


    def testSerializationOnOJ4BTnextPropertyfor3Level_TC4(self):
        # arrange
        bintree = "{1,2,3,4,#,#,5}"
        rulst = self.testedobj.DeserializationOnOJ(bintree)
        self.assertEqual(rulst, True)

        expSrlztn = "{1,#,2,3,#,4,5,#}"

        # act
        actSrlztn = self.testedobj.SerializationOnOJ4BTnextProperty()

        # assert
        self.assertEqual(expSrlztn, actSrlztn)


    def testSerializationOnOJ4BTnextPropertyfor3Level_TC5(self):
        # arrange
        bintree = "{1,2,3,#,4,#,5}"
        rulst = self.testedobj.DeserializationOnOJ(bintree)
        self.assertEqual(rulst, True)

        expSrlztn = "{1,#,2,3,#,4,5,#}"

        # act
        actSrlztn = self.testedobj.SerializationOnOJ4BTnextProperty()

        # assert
        self.assertEqual(expSrlztn, actSrlztn)


    def testSearchBST_TC1(self):
        # arrange
        val = 2
        expRslt = None

        # act
        actRslt = self.testedobjbst.searchBST(None, val)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearchBST_TC2(self):
        # arrange
        bstree = "{2,1,3}"
        self.bst.DeserializationOnOJ(bstree)

        val = 2
        expRslt = self.bst.rootnode

        # act
        actRslt = self.testedobjbst.searchBST(self.bst.rootnode, val)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearchBST_TC3(self):
        # arrange
        bstree = "{2,1,3}"
        self.bst.DeserializationOnOJ(bstree)

        val = 1
        expRslt = self.bst.rootnode.left

        # act
        actRslt = self.testedobjbst.searchBST(self.bst.rootnode, val)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearchBST_TC4(self):
        # arrange
        bstree = "{2,1,3}"
        self.bst.DeserializationOnOJ(bstree)

        val = 3
        expRslt = self.bst.rootnode.right

        # act
        actRslt = self.testedobjbst.searchBST(self.bst.rootnode, val)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearchBST_TC5(self):
        # arrange
        bstree = "{2,1,3}"
        self.bst.DeserializationOnOJ(bstree)

        val = 4
        expRslt = None

        # act
        actRslt = self.testedobjbst.searchBST(self.bst.rootnode, val)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearchBST_TC6(self):
        # arrange
        bstree = "{7,2,13,#,5}"
        self.bst.DeserializationOnOJ(bstree)

        val = 5
        expRslt = self.bst.rootnode.left.right

        # act
        actRslt = self.testedobjbst.searchBST(self.bst.rootnode, val)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testInsertValToBST_TC1(self):
        # arrange
        bstree = "{}"
        self.bst.DeserializationOnOJ(bstree)
        self.assertEqual(None, self.bst.rootnode)

        val = 2
        expRslt = "{2}"

        # act
        self.bst.rootnode = self.testedobjbst.insertValToBST(self.bst.rootnode, val)

        # assert
        actRslt = self.bst.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testInsertValToBST_TC2(self):
        # arrange
        bstree = "{2}"
        self.bst.DeserializationOnOJ(bstree)

        val = 1
        expRslt = "{2,1}"

        # act
        self.bst.rootnode = self.testedobjbst.insertValToBST(self.bst.rootnode, val)

        # assert
        actRslt = self.bst.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testInsertValToBST_TC3(self):
        # arrange
        bstree = "{2}"
        self.bst.DeserializationOnOJ(bstree)

        val = 3
        expRslt = "{2,#,3}"

        # act
        self.bst.rootnode = self.testedobjbst.insertValToBST(self.bst.rootnode, val)

        # assert
        actRslt = self.bst.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testInsertValToBST_TC4(self):
        # arrange
        bstree = "{2}"
        self.bst.DeserializationOnOJ(bstree)

        val = 2
        expRslt = "{2}"

        # act
        self.bst.rootnode = self.testedobjbst.insertValToBST(self.bst.rootnode, val)

        # assert
        actRslt = self.bst.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testInsertValToBST_TC5(self):
        # arrange
        bstree = "{5,2,9,#,#,7,19}"
        self.bst.DeserializationOnOJ(bstree)

        val = 13
        expRslt = "{5,2,9,#,#,7,19,#,#,13}"

        # act
        self.bst.rootnode = self.testedobjbst.insertValToBST(self.bst.rootnode, val)

        # assert
        actRslt = self.bst.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testGenerateBST_TC1(self):
        # arrange
        bstree = "{}"
        self.bst.DeserializationOnOJ(bstree)

        vallist = [1,2,3]
        expRslt = "{1,#,2,#,3}"

        # act
        self.bst.rootnode = self.testedobjbst.generateBST(vallist)

        # assert
        actRslt = self.bst.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testGenerateBST_TC2(self):
        # arrange
        bstree = "{}"
        self.bst.DeserializationOnOJ(bstree)

        vallist = [1,3,2]
        expRslt = "{1,#,3,2}"

        # act
        self.bst.rootnode = self.testedobjbst.generateBST(vallist)

        # assert
        actRslt = self.bst.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testGenerateBST_TC3(self):
        # arrange
        bstree = "{}"
        self.bst.DeserializationOnOJ(bstree)

        vallist = [2,1,3]
        expRslt = "{2,1,3}"

        # act
        self.bst.rootnode = self.testedobjbst.generateBST(vallist)

        # assert
        actRslt = self.bst.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testGenerateBST_TC4(self):
        # arrange
        bstree = "{}"
        self.bst.DeserializationOnOJ(bstree)

        vallist = [2,3,1]
        expRslt = "{2,1,3}"

        # act
        self.bst.rootnode = self.testedobjbst.generateBST(vallist)

        # assert
        actRslt = self.bst.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testGenerateBST_TC5(self):
        # arrange
        bstree = "{}"
        self.bst.DeserializationOnOJ(bstree)

        vallist = [3,1,2]
        expRslt = "{3,1,#,#,2}"

        # act
        self.bst.rootnode = self.testedobjbst.generateBST(vallist)

        # assert
        actRslt = self.bst.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


    def testGenerateBST_TC6(self):
        # arrange
        bstree = "{}"
        self.bst.DeserializationOnOJ(bstree)

        vallist = [3,2,1]
        expRslt = "{3,2,#,1}"

        # act
        self.bst.rootnode = self.testedobjbst.generateBST(vallist)

        # assert
        actRslt = self.bst.SerializationOnOJ()
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
