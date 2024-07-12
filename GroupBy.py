import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Downloads\weather_by_cities.csv")
#print (df)

a = df.groupby ('city')
for city, city_df in a:
    print (city)
    print (city_df)

#! To get specfic city DF

#a.get_group ('paris')   #!weather details of Paris is retrieved
#print (city_df)

#! Q - What is the maximum temp. in each of the city?

m = a.max()
print (m)   #! SPLIT - APPLY - COMBINE was executed

#! - What is the average windspeed in each of the city?

b = a[['windspeed']].mean()
print(b)

c = a.describe().T   #Here ".T" is used to transpose the output table for better visualization.
print (c)

import matplotlib.pyplot as plt
d = a[['temperature', 'windspeed']].plot()
plt.title ('city')
plt.show()