'''
Created on Jan 1, 2015

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


    def testCompareVersion_TC1(self):
        #arrange
        version1 = "1.0"
        version2 = "1.0"
        expRslt = 0

        #act
        actRslt = self.testedobj.compareVersion(version1, version2)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCompareVersion_TC2(self):
        #arrange
        version1 = "0.1"
        version2 = "1.1"
        expRslt = -1

        #act
        actRslt = self.testedobj.compareVersion(version1, version2)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCompareVersion_TC3(self):
        #arrange
        version1 = "1.2"
        version2 = "1.1"
        expRslt = 1

        #act
        actRslt = self.testedobj.compareVersion(version1, version2)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCompareVersion_TC4(self):
        #arrange
        version1 = "1.2.3"
        version2 = "1.1.0"
        expRslt = 1

        #act
        actRslt = self.testedobj.compareVersion(version1, version2)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCompareVersion_TC5(self):
        #arrange
        version1 = "1.2.3"
        version2 = "2.1.0"
        expRslt = -1

        #act
        actRslt = self.testedobj.compareVersion(version1, version2)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCompareVersion_TC6(self):
        #arrange
        version1 = "2.2.3"
        version2 = "2.2.3"
        expRslt = 0

        #act
        actRslt = self.testedobj.compareVersion(version1, version2)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCompareVersion_TC7(self):
        #arrange
        version1 = "01"
        version2 = "1"
        expRslt = 0

        #act
        actRslt = self.testedobj.compareVersion(version1, version2)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCompareVersion_TC8(self):
        #arrange
        version1 = "01"
        version2 = "1.2"
        expRslt = -1

        #act
        actRslt = self.testedobj.compareVersion(version1, version2)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCompareVersion_TC9(self):
        #arrange
        version1 = "01.2.3"
        version2 = "1.2"
        expRslt = 1

        #act
        actRslt = self.testedobj.compareVersion(version1, version2)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCompareVersion_TC10(self):
        #arrange
        version1 = "01.2.3"
        version2 = "1.2.03"
        expRslt = 0

        #act
        actRslt = self.testedobj.compareVersion(version1, version2)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testCompareVersion_TC11(self):
        #arrange
        version1 = "1"
        version2 = "1.0"
        expRslt = 0

        #act
        actRslt = self.testedobj.compareVersion(version1, version2)

        #assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
