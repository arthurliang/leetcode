'''
Created on Jan 24, 2015

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


    def testConvertToTitle_TC1(self):
        # arrange
        rowIndex = 0
        expRslt = [1]

        # act
        actRslt = self.testedobj.getRow(rowIndex)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitle_TC2(self):
        # arrange
        rowIndex = 1
        expRslt = [1, 1]

        # act
        actRslt = self.testedobj.getRow(rowIndex)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitle_TC3(self):
        # arrange
        rowIndex = 3
        expRslt = [1, 3, 3, 1]

        # act
        actRslt = self.testedobj.getRow(rowIndex)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertToTitle_TC4(self):
        # arrange
        rowIndex = 5
        expRslt = [1, 5, 10, 10, 5, 1]

        # act
        actRslt = self.testedobj.getRow(rowIndex)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
