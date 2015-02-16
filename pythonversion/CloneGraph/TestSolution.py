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


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
