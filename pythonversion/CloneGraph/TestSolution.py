'''
Created on Feb 16, 2015

@author: Arthur
'''
import unittest
import Solution
from utility.Graph import Graph

class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        self.dataGraph = Graph()
        self.rsltGraph = Graph()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testCloneGraph_TC1(self):
        # arrange
        node = None

        # act
        actNode = self.testedobj.cloneGraph(node)

        # assert
        self.assertEqual(None, actNode)


    def testCloneGraph_TC2(self):
        # arrange
        expRslt = "{1}"
        self.dataGraph.DeserializationOnOJ(expRslt)

        # act
        actNode = self.testedobj.cloneGraph(self.dataGraph.nodelist[0])

        # assert
        self.rsltGraph.nodelist.append(actNode)
        actRslt = self.rsltGraph.SerializationOnOJ()

        for actgn in self.rsltGraph.nodelist:
            self.assertNotIn(actgn, self.dataGraph.nodelist)
        self.assertEqual(expRslt, actRslt)


    def testCloneGraph_TC3(self):
        # arrange
        expRslt = "{1,2#2}"
        self.dataGraph.DeserializationOnOJ(expRslt)

        # act
        actNode = self.testedobj.cloneGraph(self.dataGraph.nodelist[0])

        # assert
        self.rsltGraph.nodelist.append(actNode)
        actRslt = self.rsltGraph.SerializationOnOJ()

        for actgn in self.rsltGraph.nodelist:
            self.assertNotIn(actgn, self.dataGraph.nodelist)
        self.assertEqual(expRslt, actRslt)


    def testCloneGraph_TC4(self):
        # arrange
        expRslt = "{0,1,2#1,2#2,2}"
        self.dataGraph.DeserializationOnOJ(expRslt)

        # act
        actNode = self.testedobj.cloneGraph(self.dataGraph.nodelist[0])

        # assert
        self.rsltGraph.nodelist.append(actNode)
        actRslt = self.rsltGraph.SerializationOnOJ()

        for actgn in self.rsltGraph.nodelist:
            self.assertNotIn(actgn, self.dataGraph.nodelist)
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
