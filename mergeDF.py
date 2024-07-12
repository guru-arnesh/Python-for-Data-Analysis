import pandas as pd
df1 = pd.DataFrame({
    "city": ["new york","chicago","orlando"],
    "temperature": [21,14,35],
})
print (df1)
print('')

df2 = pd.DataFrame({
    "city": ["chicago","new york","orlando"],
    "humidity": [65,68,75],
})
print (df2)
print('')

df = pd.merge(df1, df2, on='city')   # this is same as inner join or intersection (just like in SQL)
print (df)
print('')


df3 = pd.merge(df1, df2, on="city", how="outer")   # performs outer join (Union)
print (df3)
print('')

df4 = pd.merge (df1,df2, on='city', how='left', indicator=True)  # the indicator function shows which data is from which table
print (df4)