
#! importing .CSV File

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
print (df)

#! Creating DataFrame from Python dictionary

import pandas as pd
weather_data ={
    'day': ['1/1/2017','1/2/2017','1/3/2017','1/4/2017','1/5/2017','1/6/2017'],
    'temperature': [32,35,28,24,32,35],
    'windspeed': [6,7,2,7,4,2],
    'event': ['Rain', 'Sunny', 'Snow','Snow','Rain', 'Sunny']
}
df = pd.DataFrame(weather_data)
print(df)

#! To check the no. of Rows & Columns

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
print (df)
print(df.shape)  #[shows no. of rows and columns]

#! To print Specified no. of rows

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
print(df.head(3))  #[diplays only 3 rows form the entire DF]

#! To print last 5 rows from a DataFrame

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
print(df.tail())  #Prints last 5 rows

#! To print specified no. of Rows from Bottom

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
print(df.tail(3))  #Prints last 3 Rows

#! To print the all the Columns

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
print(df.columns)  #prints all column names
print(df.day)  #prints all the values in DAY column

#! TYPES

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
print(df)
print(type(df.day))

#! To print specific columns 

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
print(df[['event', 'day']])  #Only prints column event & day
#! OPERATIONS

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
print(df.temperature.max())

#! STATISTICS

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
print (df)
print (df.describe())

#! CONDITIONS

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
print (df[df.temperature >= 32 ])  #prints temp values>=32

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
print (df[df.temperature == df.temperature.max()])  #prints entire row where temp. is max

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
print (df.day[df.temperature == df.temperature.max()])  #only shows date when the temp. is max

#! INDEX

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
print (df.index)  #displays the order of indexin

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
df.set_index('day')
print(df)  #DataFrame modified with DAY as index

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
(df.set_index('day', inplace=True))
print (df.loc['01-03-2017'])  #shows details on specified date

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
df.reset_index
print(df)  #index has been reset, will show original DataFrame