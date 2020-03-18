
# (function approach)

import pandas



def add_state_names():
    pass


if __name__ == "main":

    df = pandas.DAtaFrame({"abbrev": ["CA", "CT", "CO", "TX", "DC"]})
    print(df.head())

    df2 = pandas.DAtaFrame({"abbrev": ["OH", "MI", "CO", "TX", "PA"]})
    print(df2.head())