

import unittest

from my_lambdata.assignment import CustomFrame

class TestCustomFrame(unittest.TestCase):

    def test_add_state_names(self):
        custom_df = CustomFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
        # assert "name" should be a column
        self.assertTrue('name'not in list(custom_df.columns))
    
        
        
        custom_df.add_state_names()
        # assert "name" should be a column
        self.assertTrue('name' in list(custom_df.columns))
        # assert "California" should exist in a column call
        # assert that first row ,name is "Cali" and "abbrev" is "CA"
       
        self.assertEqual(custom_df['name'][0], "Cali")
        self.assertEqual(custom_df['abbrev'][0], "CA")
    
        
    

    
if __name__ == "__main__":
    unittest.main()



