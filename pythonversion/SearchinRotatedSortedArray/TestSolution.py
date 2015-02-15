'''
Created on Feb 15, 2015

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


    def testSearch_TC1(self):
        # arrange
        A = []
        target = 0
        expRslt = -1

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearch_TC2(self):
        # arrange
        A = None
        target = 0
        expRslt = -1

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearch_TC3(self):
        # arrange
        A = [1]
        target = 1
        expRslt = 0

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearch_TC4(self):
        # arrange
        A = [1,0]
        target = 0
        expRslt = 1

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearch_TC5(self):
        # arrange
        A = [1,-1,0]
        target = 0
        expRslt = 2

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearch_TC6(self):
        # arrange
        A = [1,2,0]
        target = 0
        expRslt = 2

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearch_TC7(self):
        # arrange
        A = [1,2,0]
        target = -2
        expRslt = -1

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearch_TC8(self):
        # arrange
        A = [1,3,0]
        target = 2
        expRslt = -1

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearch_TC9(self):
        # arrange
        A = [1,2,0]
        target = 2
        expRslt = 1

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearch_TC10(self):
        # arrange
        A = [0,1,-1]
        target = 2
        expRslt = -1

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearch_TC11(self):
        # arrange
        A = [0,1,-3,-2,-1]
        target = 1
        expRslt = 1

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearch_TC12(self):
        # arrange
        A = [5,1,3]
        target = 2
        expRslt = -1

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearch_TC13(self):
        # arrange
        A = [1,3,5]
        target = 5
        expRslt = 2

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearch_TC14(self):
        # arrange
        A = [4,5,6,7,0,1,2]
        target = 0
        expRslt = 4

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearch_TC15(self):
        # arrange
        A = [7,8,1,2,3,4,5,6]
        target = 2
        expRslt = 3

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testSearch_TC16(self):
        # arrange
        A = [7,8,9,10,11,12,5,6]
        target = 12
        expRslt = 5

        # act
        actRslt = self.testedobj.search(A, target)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()