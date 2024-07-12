'''Contigency table, also known as cross tabulation or crosstab is type of table in a matrix format that displays
the frequency distribution of the tables. '''

import pandas as pd
import numpy as np
df = pd.read_excel (r"C:\Users\gurua\Downloads\survey.xls")
print (df)
print ('')

df1 = pd.crosstab (df.Nationality, df. Handedness)  #crosstab on the basis of nationality
print (df1)
print ('')

df2 = pd.crosstab (df.Sex, df.Handedness)  #crosstab on the basis of sex
print (df2)
print ('')

df3 = pd.crosstab (df.Sex, df.Handedness, margins=True)  #shows the count in a different column
print (df3)
print ('')

df4 = pd.crosstab ([df.Sex], [df.Handedness],normalize='index')
print (df4)
print ('')

df5 = pd.crosstab (df.Sex, df.Handedness, values=df.Age, aggfunc=np.average)
print (df5)