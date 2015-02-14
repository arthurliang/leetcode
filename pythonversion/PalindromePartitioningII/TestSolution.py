'''
Created on Feb 14, 2015

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


    def testMinCut_TC1(self):
        # arrange
        s = "a"
        expRslt = 0

        # act
        actRslt = self.testedobj.minCut(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testMinCut_TC2(self):
        # arrange
        s = "aa"
        expRslt = 0

        # act
        actRslt = self.testedobj.minCut(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testMinCut_TC3(self):
        # arrange
        s = "aaa"
        expRslt = 0

        # act
        actRslt = self.testedobj.minCut(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testMinCut_TC4(self):
        # arrange
        s = "aaaa"
        expRslt = 0

        # act
        actRslt = self.testedobj.minCut(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testMinCut_TC5(self):
        # arrange
        s = "aab"
        expRslt = 1

        # act
        actRslt = self.testedobj.minCut(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testMinCut_TC6(self):
        # arrange
        s = "aba"
        expRslt = 0

        # act
        actRslt = self.testedobj.minCut(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testMinCut_TC7(self):
        # arrange
        s = "ababa"
        expRslt = 0

        # act
        actRslt = self.testedobj.minCut(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testMinCut_TC8(self):
        # arrange
        s = "ababababababababababababcbabababababababababababa"
        expRslt = 0

        # act
        actRslt = self.testedobj.minCut(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testMinCut_TC9(self):
        # arrange
        s = "ccaacabacb"
        expRslt = 3

        # act
        actRslt = self.testedobj.minCut(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testMinCut_TC10(self):
        # arrange
        s = "aaabaa"
        expRslt = 1

        # act
        actRslt = self.testedobj.minCut(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testMinCut_TC11(self):
        # arrange
        s = "fifgbeajcacehiicccfecbfhhgfiiecdcjjffbghdidbhbdbfbfjccgbbdcjheccfbhafehieabbdfeigbiaggchaeghaijfbjhi"
        expRslt = 75

        # act
        actRslt = self.testedobj.minCut(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testMinCut_TC12(self):
        # arrange
        s = "ab"
        expRslt = 1

        # act
        actRslt = self.testedobj.minCut(s)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
