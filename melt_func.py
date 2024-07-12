import pandas as pd
df = pd.read_csv (r"C:\Users\gurua\Downloads\weather_melt.csv")
print (df)
print('')

df1 = pd.melt (df, id_vars=['day'], var_name='city', value_name='temperature')
print (df1)