
# (function approach)

import pandas

class DataProcessor():
    def __init__(self,my_df)
    """
    param: my_df (pandas.DayaFrame) containing a column called "abbrev"
    """
    self.df = my_df

def add_state_names(my_df):
    
    """
     Adds corresponding state names to a dataframe.
     param: my_df (pandas.DayaFrame) containing a column called "abbrev"

    """
    
    new_df = my_df.copy()

    names_map = {
        "CA" : "Cali",
        "CT" : "Conn",
        "CO" : "Colorado"
    }
    # new_df["name"] = new_df["abbrev"].map(names_map)
    # return new_df
    processor = DataProcessor(df)
    processor.add_state_names()
    print (processor.df.head())

    
if __name__ == "__main__":

    print ("_______________________")
    df = pandas.DataFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    # print(df.head())
    # new_df = add_state_names(df)
    # print(new_df.head())
    processor = DataProcessor(df)
    print(processor.df.head())


    print ("_______________________")

    df2 = pandas.DataFrame({"abbrev": ["OH", "MI", "CO", "TX", "PA"]})
    print(df2.head())
    new_df2 = add_state_names(df2)
    print(new_df2.head())