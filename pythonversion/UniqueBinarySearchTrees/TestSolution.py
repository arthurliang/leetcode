'''
Created on Feb 9, 2015

@author: Arthur
'''
import unittest
import Solution


class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testNumTrees_TC1(self):
        # arrange
        n = 0
        expRslt = 0

        # act
        actRslt = self.testedobj.numTrees(n)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testNumTrees_TC2(self):
        # arrange
        n = 1
        expRslt = 1

        # act
        actRslt = self.testedobj.numTrees(n)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testNumTrees_TC3(self):
        # arrange
        n = 2
        expRslt = 2

        # act
        actRslt = self.testedobj.numTrees(n)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testNumTrees_TC4(self):
        # arrange
        n = 3
        expRslt = 5

        # act
        actRslt = self.testedobj.numTrees(n)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testNumTrees_TC5(self):
        # arrange
        n = 4
        expRslt = 14

        # act
        actRslt = self.testedobj.numTrees(n)

        # assert
        self.assertEqual(expRslt, actRslt)



    def testNumTrees_TC6(self):
        # arrange
        n = 5
        expRslt = 42

        # act
        actRslt = self.testedobj.numTrees(n)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testNumTrees_TC7(self):
        # arrange
        n = 6
        expRslt = 132

        # act
        actRslt = self.testedobj.numTrees(n)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()