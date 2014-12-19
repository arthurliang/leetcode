'''
Created on Dec 19, 2014

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


    def testConvertWhenStringIsNullandNRowis1_TC1(self):
        # arrange
        s = ""
        nRows = 1
        expRslt = s

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertWhenStringIsNotNullandNRowis1_TC2(self):
        # arrange
        s = "a"
        nRows = 1
        expRslt = s

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)



    def testConvertWhenStringIsNotNullandNRowis1_TC3(self):
        # arrange
        s = "ab"
        nRows = 1
        expRslt = s

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertWhenStringHasNlettersAndNRowisN_TC1(self):
        # arrange
        s = "a"
        nRows = 1
        expRslt = s

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertWhenStringHasNlettersAndNRowisN_TC2(self):
        # arrange
        s = "ab"
        nRows = 2
        expRslt = s

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertWhenStringHasMlettersandNRowisNWhileMlessthenN_TC1(self):
        # arrange
        s = "a"
        nRows = 2
        expRslt = s

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertWhenStringHasMlettersandNRowisNWhileMlessthenN_TC2(self):
        # arrange
        s = "ab"
        nRows = 3
        expRslt = s

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertWhenStringHasMlettersandNRowisNWhileMgreatthenN_TC1(self):
        # arrange
        s = "abc"
        nRows = 2
        expRslt = "acb"

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertWhenStringHasMlettersandNRowisNWhileMgreatthenN_TC2(self):
        # arrange
        s = "abcd"
        nRows = 3
        expRslt = "abdc"

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertWhenStringHasMlettersandNRowisNWhileMgreatthenN_TC3(self):
        # arrange
        s = "abcdef"
        nRows = 3
        expRslt = "aebdfc"

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertWhenStringHasMlettersandNRowisNWhileMgreatthenN_TC4(self):
        # arrange
        s = "abcdefg"
        nRows = 3
        expRslt = "aebdfcg"

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


    def testConvertWhenStringHasMlettersandNRowisNWhileMgreatthenN_TC5(self):
        # arrange
        s = "hjouvsuyoypayulyeimuotehzriicfskpggkbbipzzrzucxamludfykgruowzgiooobppleqlwphapjnadqhdcnvwdtxjbmyppphauxnspusgdhiixqmbfjxjcvudjsuyibyebmwsiqyoygyxymzevypzvjegebeocfuftsxdixtigsieehkchzdflilrjqfnxztqrsvbspkyhsenbppkqtpddbuotbbqcwivrfxjujjddntgeiqvdgaijvwcyaubwewpjvygehljxepbpiwuqzdzubdubzvafspqpqwuzifwovyddwyvvburczmgyjgfdxvtnunneslsplwuiupfxlzbknhkwppanltcfirjcddsozoyvegurfwcsfmoxeqmrjowrghwlkobmeahkgccnaehhsveymqpxhlrnunyfdzrhbasjeuygafoubutpnimuwfjqsjxvkqdorxxvrwctdsneogvbpkxlpgdirbfcriqifpgynkrrefx"
        nRows = 503
        expRslt = "hjouvsuyoypayulyeimuotehzriicfskpggkbbipzzrzucxamludfykgruowzgiooobppleqlwphapjnadqhdcnvwdtxjbmyppphauxnspusgdhiixqmbfjxjcvudjsuyibyebmwsiqyoygyxymzevypzvjegebeocfuftsxdixtigsieehkchzdflilrjqfnxztqrsvbspkyhsenbppkqtpddbuotbbqcwivrfxjujjddntgeiqvdgaijvwcyaubwewpjvygehljxepbpiwuqzdzubdubzvafspqpqwuzifwovyddwyvvburczmgyjgfdxvtnunneslsplwuiupfxlzbknhkwppanltcfirjcddsozoyvegurfwcsfmoxeqmrjowrghwlkobmeahkgccnaehhsveymqpxhlrnunyfdzrhbasjeuygafoubutpnimuwfjqsjxvkqdorxxvrwctdsneogvbpkxlpgdirbfcriqifpgynkrxrfe"

        # act
        actRslt = self.testedobj.convert(s, nRows)

        # assert
        self.assertEqual(expRslt, actRslt)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
