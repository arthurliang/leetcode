'''
Created on Feb 13, 2015

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


    def testPartition_TC1(self):
        # arrange
        s = "a"
        expRslt = [["a"]
                   ]

        # act
        actRslt = self.testedobj.partition(s)

        # assert
        self.assertItemsEqual(expRslt, actRslt)


    def testPartition_TC2(self):
        # arrange
        s = "aa"
        expRslt = [["a", "a"],
                   ["aa"]
                   ]

        # act
        actRslt = self.testedobj.partition(s)

        # assert
        self.assertItemsEqual(expRslt, actRslt)


    def testPartition_TC3(self):
        # arrange
        s = "aaa"
        expRslt = [["a", "a", "a"],
                   ["aa", "a"],
                   ["a", "aa"],
                   ["aaa"]
                   ]

        # act
        actRslt = self.testedobj.partition(s)

        # assert
        self.assertItemsEqual(expRslt, actRslt)


    def testPartition_TC4(self):
        # arrange
        s = "aaaa"
        expRslt = [["a", "a", "a", "a"],
                   ["aa", "a", "a"],
                   ["aa", "aa"],
                   ["a", "aa", "a"],
                   ["a", "a", "aa"],
                   ["aaa", "a"],
                   ["a", "aaa"],
                   ["aaaa"]
                   ]

        # act
        actRslt = self.testedobj.partition(s)

        # assert
        self.assertItemsEqual(expRslt, actRslt)


    def testPartition_TC5(self):
        # arrange
        s = "aab"
        expRslt = [["a", "a", "b"],
                   ["aa", "b"]
                   ]

        # act
        actRslt = self.testedobj.partition(s)

        # assert
        self.assertItemsEqual(expRslt, actRslt)


    def testPartition_TC6(self):
        # arrange
        s = "aba"
        expRslt = [["aba"],
                   ["a", "b", "a"]
                   ]

        # act
        actRslt = self.testedobj.partition(s)

        # assert
        self.assertItemsEqual(expRslt, actRslt)


    def testPartition_TC7(self):
        # arrange
        s = "ababa"
        expRslt = [['ababa'],
                   ['aba', 'b', 'a'],
                   ['a', 'bab', 'a'],
                   ['a', 'b', 'aba'],
                   ['a', 'b', 'a', 'b', 'a']
                   ]

        # act
        actRslt = self.testedobj.partition(s)

        # assert
        self.assertItemsEqual(expRslt, actRslt)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
