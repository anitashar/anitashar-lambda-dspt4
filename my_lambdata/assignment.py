
# (function approach)

import pandas

class CustomFrame(pandas.DataFrame):
    # def __init__(self,my_df):
    #     """
    #     param: my_df (pandas.DayaFrame) containing a column called "abbrev"
    #     """
    #     self.df = my_df.copy()

    def add_state_names(self):
        
        """
        Adds corresponding state names to a dataframe.
        param: my_df (pandas.DayaFrame) containing a column called "abbrev"

        """
        
        # new_df = self.df.copy()

        names_map = {
            "CA" : "Cali",
            "CT" : "Conn",
            "CO" : "Colorado"
        }
        self.df["name"] =   self.df["abbrev"].map(names_map)
        
    

    
if __name__ == "__main__":

    print ("_______________________")
    df1 = pandas.DataFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    # print(df1.head())
    # new_df = add_state_names(df1)
    # print(new_df.head())


    # processor = DataProcessor(df1)
    # print(processor.df.head())
    # processor.add_state_names()
    # print(processor.df.head())

    custom_df = CustomFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    print(custom_df.head())
    # custom_df.add_state_names()
    # print(custom_df.head())


    print ("_______________________")

    # df2 = pandas.DataFrame({"abbrev": ["OH", "MI", "CO", "TX", "PA"]})
    # print(df2.head())
    # new_df2 = add_state_names(df2)
    # print(new_df2.head())