
import unittest

from my_lambdata.my_mod import enlarge


class TestMyMod(unittest.Testcase):
    
    def test_enlarge(self):
        self.assertEquaal(enlarge(5),500)



if __name__ = '__main__':
    unittest.main()

