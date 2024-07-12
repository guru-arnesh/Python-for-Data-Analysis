import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Downloads\weather_data.csv", parse_dates=['day'])
(type(df.day[0]))
df.set_index ('day', inplace=True)  #!setting day column as reference index
print (df)

new_df = df.fillna(0)  #!replaces NaN value with 0
print (new_df)

new_df = df.fillna({      #!replacing specific column with custom values.
    'temperature': 0,
    'windspeed': '0mph',
    'event' : 'no_event'
})
print (new_df)

new_df = df.fillna(method = 'ffill')  #!carries forward the previous value into NaN
print (new_df)

new_df = (df                          #!assigning method using python dictionary 
      .assign(temperature=df['temperature'].fillna(method='bfill'))
      .assign(windspeed=df['windspeed'].fillna(method='ffill'))
      .assign(event=df['event'].fillna('no_event')))
print(new_df)

new_df = df.interpolate()  #!applies linear interpolation to numeric data
print (new_df)

new_df = df.interpolate(method = 'time')  #!applies linear interpolation keeping time as a contraint
print (new_df)

new_df = df.dropna()  #!deletes all the rows that contains NaN
print (new_df)

new_df = df.dropna(how='all')  #!drops the row which has all its value as NaN
print (new_df)

new_df = df.dropna(thresh=2)  #! drops row where <=2 NaN value
print (new_df)

new_dt = pd.date_range('2017-01-01', '2017-01-11')
idx = pd.DatetimeIndex(new_dt)
df = df.reindex(idx)
print(df)                     #! prints the new date range as index


#! REPLACE FUNCTION

import pandas as pd
import numpy as np
df = pd.read_csv (r"C:\Users\gurua\Downloads\weather_data (1).csv")
print (df)

new_df = df.replace (-99999, np.NaN)
print (new_df)          #! with replace we have to pass two paramaters

new_df = df.replace ([-99999,-88888], np.NaN)
print (new_df)          #! replaced both values with NaN together

new_df = df.replace ({
    'temperature': (-99999,-88888),
    'windspeed': -99999, 
    'event': '0'
}, np.NaN)
print (new_df)

new_df = df.replace ({
    -99999: np.NaN,      #! Here mapping is done
    '0': 'sunny',
})
print (new_df)

#! REGULAR EXPRESSIONS (regex)
#! WE WILL TAKE DIFFERENT DATA SET HERE FOR BETTER UNDERSTANDING

import pandas as pd
df = pd.read_excel (r"C:\Users\gurua\Downloads\WeatherData.xlsx")
print (df)

new_df = df.replace ('[A-Za-z]','', regex=True)  #! But this will remove the data from event column
print (new_df)

new_df = df.replace({
    'temperature': '[A-Za-z]',                   #! Now the data looks better by using regex function for specific column
    'windspeed': '[A-Za-z]',
},'',regex=True)
print (new_df)


#! REPLACING LIST OF VALUES WITH ANOTHER LIST OF VALUES

import pandas as pd
df = pd.DataFrame({
    'student': ['kunal', 'mo chen', 'alex', 'robert', 'mishra', 'guru'],
    'score': ['exceptional', 'average', 'good', 'poor', 'average', 'exceptional']
})
#df.set_index('student', inplace=True)
print(df)

new_df = df.replace (['poor', 'average', 'good', 'exceptional'], [1,2,3,4])
print (new_df)