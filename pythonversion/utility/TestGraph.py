'''
Created on Feb 16, 2015

@author: Arthur
'''
import unittest
import Graph

class Test(unittest.TestCase):

    def setUp(self):
        self.testedobj = Graph.Graph()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testGraph_Constructor(self):
        self.assertEqual(self.testedobj.nodelist, [])


    def testGraphDeserializationOnOJforParameterVerifyWithWrongPrefix(self):
        # arrange
        srlztn = "#"

        # act
        Rslt = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(Rslt, False)
        self.assertEqual([], self.testedobj.nodelist)


    def testGraphDeserializationOnOJforParameterVerifyWithWrongSurfix(self):
        # arrange
        srlztn = "{#"

        # act
        Rslt = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(Rslt, False)
        self.assertEqual([], self.testedobj.nodelist)


    def testGraphDeserializationOnOJforParameterVerifyWithSharpNoLabel_TC1(self):
        # arrange
        srlztn = "{#}"

        # act
        Rslt = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(Rslt, False)
        self.assertEqual([], self.testedobj.nodelist)


    def testGraphDeserializationOnOJforParameterVerifyWithSharpNoLabel_TC2(self):
        # arrange
        srlztn = "{#1#}"

        # act
        Rslt = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(Rslt, False)
        self.assertEqual([], self.testedobj.nodelist)


    def testGraphDeserializationOnOJforParameterVerifyWithSharpNoLabel_TC3(self):
        # arrange
        srlztn = "{1##}"

        # act
        Rslt = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(Rslt, False)
        self.assertEqual([], self.testedobj.nodelist)


    def testGraphDeserializationOnOJforParameterVerifyWithSharpNoLabel_TC4(self):
        # arrange
        srlztn = "{1##2,2}"

        # act
        Rslt = self.testedobj.DeserializationOnOJ(srlztn)

        # assert
        self.assertEqual(Rslt, False)
        self.assertEqual([], self.testedobj.nodelist)


    def testGraphDeserializationOnOJ_and_SerializationOnOJ_TC1(self):
        # arrange
        srlztn = "{}"

        # act
        Rslt = self.testedobj.DeserializationOnOJ(srlztn)
        actRslt = self.testedobj.SerializationOnOJ()

        # assert
        self.assertEqual(Rslt, True)
        self.assertEqual(srlztn, actRslt)
        self.assertEqual([], self.testedobj.nodelist)


    def testGraphDeserializationOnOJ_and_SerializationOnOJ_TC2(self):
        # arrange
        srlztn = "{1}"
        expNodeNum = 1

        # act
        Rslt = self.testedobj.DeserializationOnOJ(srlztn)
        actRslt = self.testedobj.SerializationOnOJ()

        # assert
        actNodeNum = len(self.testedobj.nodelist)
        self.assertEqual(Rslt, True)
        self.assertEqual(srlztn, actRslt)
        self.assertEqual(expNodeNum, actNodeNum)


    def testGraphDeserializationOnOJ_and_SerializationOnOJ_TC3(self):
        # arrange
        srlztn = "{1,2#2}"
        expNodeNum = 2

        # act
        Rslt = self.testedobj.DeserializationOnOJ(srlztn)
        actRslt = self.testedobj.SerializationOnOJ()

        # assert
        actNodeNum = len(self.testedobj.nodelist)
        self.assertEqual(Rslt, True)
        self.assertEqual(srlztn, actRslt)
        self.assertEqual(expNodeNum, actNodeNum)


    def testGraphDeserializationOnOJ_and_SerializationOnOJ_TC4(self):
        # arrange
        srlztn = "{0,1,2#1,2#2,2}"
        expNodeNum = 3

        # act
        Rslt = self.testedobj.DeserializationOnOJ(srlztn)
        actRslt = self.testedobj.SerializationOnOJ()

        # assert
        actNodeNum = len(self.testedobj.nodelist)
        self.assertEqual(Rslt, True)
        self.assertEqual(srlztn, actRslt)
        self.assertEqual(expNodeNum, actNodeNum)


    def testGraphSerializationOnOJ_TC1(self):
        # arrange
        self.testedobj.nodelist.append(None)
        expRslt = "{}"

        # act
        actRslt = self.testedobj.SerializationOnOJ()

        # assert
        self.assertEqual(expRslt, actRslt)


    def testGraphSerializationOnOJ_TC2(self):
        # arrange
        gn = Graph.UndirectedGraphNode(0)
        self.testedobj.nodelist.append(gn)
        expRslt = "{0}"

        # act
        actRslt = self.testedobj.SerializationOnOJ()

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
