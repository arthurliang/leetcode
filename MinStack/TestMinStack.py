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


    def testStackPushAndTop_TC1(self):
        #arrange
        data = 1

        #act
        self.testedobj.push(data)

        #assert
        self.assertEqual(data, self.testedobj.top())
        self.assertEqual(1, len(self.testedobj.backendlist))


    def testStackPushAndTop_TC2(self):
        #arrange

        #act

        #assert
        self.assertEqual(None, self.testedobj.top())
        self.assertEqual(0, len(self.testedobj.backendlist))


    def testStackPop_TC1(self):
        #arrange
        data = 1
        self.testedobj.push(data)
        expRslt = None

        #act
        actRslt = self.testedobj.pop()

        #assert
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(0, len(self.testedobj.backendlist))


    def testStackPop_TC2(self):
        #arrange
        expRslt = None

        #act
        actRslt = self.testedobj.pop()

        #assert
        self.assertEqual(expRslt, actRslt)
        self.assertEqual(0, len(self.testedobj.backendlist))


    def testStackGetMin_TC1(self):
        #arrange
        datalist = [4,1,3,4,1,2,0,7,8,65,0,4,-3,80]
        for data in datalist:
            self.testedobj.push(data)
        expRslt = -3

        #act
        actRslt = self.testedobj.getMin()

        #assert
        self.assertEqual(expRslt, actRslt)


    def FuncForEasyTest(self, inputStr):
        output = []
        actlist = inputStr.split(',')
        for act in actlist:
            if "push" in act:
                data = int(act[5:-1])
                self.testedobj.push(data)
            elif "getMin" in act:
                output.append(self.testedobj.getMin())
            else:
                getattr(self.testedobj, act)()
        return output


    def testStackGetMin_TC2(self):
        #arrange
        inputStr = "push(2),push(0),push(3),push(0),getMin,pop,getMin,pop,getMin,pop,getMin"

        expRslt = [0,0,0,2]

        #act
        actRslt = self.FuncForEasyTest(inputStr)

        #assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()