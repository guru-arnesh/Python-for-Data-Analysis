
#! Importing a .CSV file

import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Desktop\weather_data.csv")
print (df)

#! Importing an EXCEL file

import pandas as pd
df = pd.read_excel (r"C:\Users\gurua\Downloads\HouseData.xlsx")
print (df)

#! By using Dictionary

import pandas as pd
weather_data = {
    'day': ['1/1/2017','1/2/2017','1/3/2017'],
    'temperature': [32,35,28],
    'windspeed': [6,7,2],
    'event': ['Rain', 'Sunny', 'Snow']
}
df = pd.DataFrame(weather_data)
print (df)