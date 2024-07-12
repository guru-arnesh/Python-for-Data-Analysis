import pandas as pd
#df1 = pd.read_excel (r"C:\Users\gurua\Downloads\stocks.xlsx")
df2 = pd.read_excel (r"C:\Users\gurua\Downloads\stocks.xlsx", header=[0,1])
#print (df1)
#print ('')
print (df2)
print ('')
print ('')

#! The data set has two level of headers

df3 = df2.stack()
print (df3)   # By default it stacks level 1 header
print ('')
print ('')

df4 = df2.stack (level=0)   # stacks the level 0 header
print (df4)
print ('')
print ('')

df_stacked = df4
print (df_stacked)
print ('')
print ('')

df5 = df_stacked.unstack()  # reverses the stacked data frame
print (df5)

import pandas as pd
df6 = pd.read_excel (r"C:\Users\gurua\Downloads\stocks_3_levels.xlsx", header=[0,1,2])
print (df6)