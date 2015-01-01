'''
Created on Jan 1, 2015

@author: Arthur
'''
import unittest
import MinStack

class Test(unittest.TestCase):


    def setUp(self):
        self.testedobj = MinStack.MinStack()
        pass


    def tearDown(self):
        self.testedobj = None
        pass


    def testStackPushAndTop(self):
        #arrange
        data = 1

        #act
        self.testedobj.push(data)

        #assert
        self.assertEqual(data, self.testedobj.top())
        self.assertEqual(1, len(self.testedobj.backlist))


    def testStackPop(self):
        #arrange
        data = 1
        self.testedobj.push(data)
        expRslt = None

        #act
        actRslt = self.testedobj.pop()

        #assert
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(0, len(self.testedobj.backlist))


    def testStackGetMin_TC1(self):
        #arrange
        datalist = [1,2,3,4,1,2,0,7,8,65,0,4,5,6]
        for data in datalist:
            self.testedobj.push(data)
        expRslt = 0

        #act
        actRslt = self.testedobj.getMin()

        #assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()