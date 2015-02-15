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


    def testSortColors_TC1(self):
        # arrange
        A = None
        expRslt =  None

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC2(self):
        # arrange
        A = []
        expRslt =  []

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC3(self):
        # arrange
        A = [0]
        expRslt =  [0]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC4(self):
        # arrange
        A = [1,0]
        expRslt =  [0,1]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC5(self):
        # arrange
        A = [0,1]
        expRslt =  [0,1]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC6(self):
        # arrange
        A = [1,2]
        expRslt =  [1,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC7(self):
        # arrange
        A = [2,1]
        expRslt =  [1,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC8(self):
        # arrange
        A = [2,0]
        expRslt =  [0,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC9(self):
        # arrange
        A = [0,2]
        expRslt =  [0,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC10(self):
        # arrange
        A = [1,2,0]
        expRslt =  [0,1,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC11(self):
        # arrange
        A = [2,1,0]
        expRslt =  [0,1,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC12(self):
        # arrange
        A = [1,0,2]
        expRslt =  [0,1,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC13(self):
        # arrange
        A = [2,0,1]
        expRslt =  [0,1,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC14(self):
        # arrange
        A = [0,1,2]
        expRslt =  [0,1,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC15(self):
        # arrange
        A = [0,2,1]
        expRslt =  [0,1,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC16(self):
        # arrange
        A = [1,1,0,0]
        expRslt =  [0,0,1,1]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC17(self):
        # arrange
        A = [0,0,1,1,2,2]
        expRslt =  [0,0,1,1,2,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC18(self):
        # arrange
        A = [1,0,0,1,2,2]
        expRslt =  [0,0,1,1,2,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC19(self):
        # arrange
        A = [1,0,1,0,2,2]
        expRslt =  [0,0,1,1,2,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


    def testSortColors_TC20(self):
        # arrange
        A = [1,0,2,2,1,0]
        expRslt =  [0,0,1,1,2,2]

        # act
        self.testedobj.sortColors(A)

        # assert
        self.assertEqual(expRslt, A)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
