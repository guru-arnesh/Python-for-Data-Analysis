import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Downloads\weather.csv")
print (df)
print ('')

#! PIVOT

df1 = df.pivot (index = 'date', columns='city')  #pivot fucntion
print (df1)
print ('')

df2 = df.pivot (index = 'date', columns='city', values='temperature')  #values parameter passed to retrieve specific column
print (df2)
print ('')

#! PIVOT TABLE

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Downloads\weather2.csv")
print (df)
print ('')

#! To find the average temp. and humidity throughout the day.

df3 = df.pivot_table(index='city', columns='date')  # data aggregated
print (df3)
print ('')

df4 = df.pivot_table(index='city', columns='date', aggfunc=max)  # by passing 'aggfunc=' we can do different operation, by-default it is average.
print (df4)
print ('')

#! GROUPER

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Downloads\weather3.csv")
df['date'] = pd.to_datetime(df['date'])
print (df)
print ('')

df5 = df.pivot_table (index=pd.Grouper(freq='M', key='date'), columns='city')  #grouper function used to find average by adding filter month wise and date wise
print (df5)