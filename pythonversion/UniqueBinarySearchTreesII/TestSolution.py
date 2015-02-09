'''
Created on Feb 9, 2015

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


    def testGenerateTrees_TC1(self):
        # arrange
        n = 0
        expRslt = ['{}']

        # act
        actLsitRslt = self.testedobj.generateTrees(n)

        # assert
        bt = BinTree()
        actRslt = [bt.SerializationOnOJbyPara(x) for x in actLsitRslt]
        self.assertEqual(expRslt, actRslt)


    def testGenerateTrees_TC2(self):
        # arrange
        n = 1
        expRslt = ['{1}']

        # act
        actLsitRslt = self.testedobj.generateTrees(n)

        # assert
        bt = BinTree()
        actRslt = [bt.SerializationOnOJbyPara(x) for x in actLsitRslt]
        self.assertEqual(expRslt, actRslt)


    def testGenerateTrees_TC3(self):
        # arrange
        n = 2
        expRslt = ['{1,#,2}', '{2,1}']

        # act
        actLsitRslt = self.testedobj.generateTrees(n)

        # assert
        bt = BinTree()
        actRslt = [bt.SerializationOnOJbyPara(x) for x in actLsitRslt]
        self.assertEqual(expRslt, actRslt)


    def testGenerateTrees_TC4(self):
        # arrange
        n = 3
        expRslt = ['{1,#,2,#,3}', '{1,#,3,2}', '{2,1,3}', '{3,1,#,#,2}', '{3,2,#,1}']

        # act
        actLsitRslt = self.testedobj.generateTrees(n)

        # assert
        bt = BinTree()
        actRslt = [bt.SerializationOnOJbyPara(x) for x in actLsitRslt]
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()