'''
Created on Jan 23, 2015

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


    def testIsValid_TC1(self):
        # arrange
        s = '('
        expRslt = False

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValid_TC2(self):
        # arrange
        s = '()'
        expRslt = True

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValid_TC3(self):
        # arrange
        s = '{'
        expRslt = False

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValid_TC4(self):
        # arrange
        s = '{}'
        expRslt = True

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValid_TC5(self):
        # arrange
        s = '['
        expRslt = False

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValid_TC6(self):
        # arrange
        s = '[]'
        expRslt = True

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValid_TC7(self):
        # arrange
        s = ')'
        expRslt = False

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValid_TC8(self):
        # arrange
        s = '}'
        expRslt = False

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValid_TC9(self):
        # arrange
        s = ']'
        expRslt = False

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValid_TC10(self):
        # arrange
        s = '([])'
        expRslt = True

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValid_TC11(self):
        # arrange
        s = '({})'
        expRslt = True

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValid_TC12(self):
        # arrange
        s = '([{}])'
        expRslt = True

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValid_TC13(self):
        # arrange
        s = '({[]})'
        expRslt = True

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValid_TC14(self):
        # arrange
        s = '([]})'
        expRslt = False

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValid_TC15(self):
        # arrange
        s = '({[])'
        expRslt = False

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testIsValid_TC16(self):
        # arrange
        s = '(){}[]()'
        expRslt = True

        # act
        actRslt = self.testedobj.isValid(s)

        # assert
        self.assertEqual(expRslt, actRslt)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()