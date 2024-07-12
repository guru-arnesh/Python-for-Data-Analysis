import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Downloads\stock_data.csv")
print (df)

#! To skip rows from a dataset

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Downloads\stock_data.csv", skiprows=1)  #skips row no. 1
print (df)

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Downloads\stock_data.csv", header=1)  #starts from row no.2
print (df)

