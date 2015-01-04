'''
Created on Jan 3, 2015

@author: Arthur
'''
import unittest
import Solution

class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = Solution.Solution()
        pass


    def tearDown(self):
        pass


    def testAtoI_TC1_1(self):
        # arrange
        s = ""
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC1_2(self):
        # arrange
        s = "   "
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC2_1(self):
        # arrange
        s = "+"
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC2_2(self):
        # arrange
        s = " +"
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC2_3(self):
        # arrange
        s = " +  "
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC3_1(self):
        # arrange
        s = "-"
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC3_2(self):
        # arrange
        s = "  -"
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC3_3(self):
        # arrange
        s = "  -       "
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC4_1(self):
        # arrange
        s = "+ 123"
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC4_2(self):
        # arrange
        s = "- 321"
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC4_3(self):
        # arrange
        s = "+-1"
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC4_4(self):
        # arrange
        s = "-+23"
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC5_1(self):
        # arrange
        s = "2 3"
        expRslt = 2

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC5_2(self):
        # arrange
        s = "12 3"
        expRslt = 12

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC5_3(self):
        # arrange
        s = "12+ 3"
        expRslt = 12

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC5_4(self):
        # arrange
        s = "12a +3"
        expRslt = 12

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC5_5(self):
        # arrange
        s = "345- +5"
        expRslt = 345

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC6_1(self):
        # arrange
        s = "a"
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC6_2(self):
        # arrange
        s = "Z"
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC6_3(self):
        # arrange
        s = "  a"
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC6_4(self):
        # arrange
        s = "  Z  "
        expRslt = 0

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC7_1(self):
        # arrange
        s = "1"
        expRslt = 1

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC7_2(self):
        # arrange
        s = "  1"
        expRslt = 1

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC7_3(self):
        # arrange
        s = "  1   "
        expRslt = 1

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC7_4(self):
        # arrange
        s = "  1234509876 "
        expRslt = 1234509876

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC7_5(self):
        # arrange
        s = "  -1876923450 "
        expRslt = -1876923450

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC8_1(self):
        # arrange
        s = "2147483647"
        expRslt = 2147483647

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC8_2(self):
        # arrange
        s = "-2147483648"
        expRslt = -2147483648

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC9_1(self):
        # arrange
        s = "2147483648"
        expRslt = 2147483647

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testAtoI_TC9_2(self):
        # arrange
        s = "-2147483649"
        expRslt = -2147483648

        # act
        actRslt = self.testedobj.atoi(s)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
