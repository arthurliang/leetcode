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
        version1 = 1.0
        version2 = 1.0
        expRslt = 0

        #act
        actRslt = self.testedobj.compareVersion(version1, version2)

        #assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
