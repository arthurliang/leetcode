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


    def testAddBinary_TC1(self):
        #arrange
        a = '11'
        b = '1'
        expRslt = '100'

        #act
        actRslt = self.testedobj.addBinary(a, b)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testAddBinary_TC2(self):
        #arrange
        a = '1'
        b = '0'
        expRslt = '1'

        #act
        actRslt = self.testedobj.addBinary(a, b)

        #assert
        self.assertEqual(expRslt, actRslt)


    def testAddBinary_TC3(self):
        #arrange
        a = '11'
        b = '11'
        expRslt = '110'

        #act
        actRslt = self.testedobj.addBinary(a, b)

        #assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
