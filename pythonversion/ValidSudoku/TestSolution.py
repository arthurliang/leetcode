'''
Created on Feb 6, 2015

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


    def testIsValidSudoku_TC1(self):
        #arrange
        board = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
        expRslt = True

        #act
        actRslt = self.testedobj.isValidSudoku(board)

        #assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()