import pandas as pd

india_weather = pd.DataFrame({
    'city' : ['mumbai','delhi','pune'],
    'temperature' : [32,45,30],
    'humidity' : [80,60,78]
})
print (india_weather)
print ('')

us_weather = pd.DataFrame({
    'city' : ['new york','chicago','orlando'],
    'temperature' : [21,14,35],
    'humidity' : [68,65,75]
})
print (us_weather)
print ('') 

df = pd.concat ([india_weather, us_weather])  # merges two DF with original index
print (df)
print ('')

df = pd.concat ([india_weather, us_weather], ignore_index=True)  # merges two DF with continuous index
print (df)
print ('')

df = pd.concat ([india_weather, us_weather], keys=['india', 'us'])
print (df)
print ('')

df = df.loc['india']  #retrieves only India data
print (df)
print ('')

temperature_df = pd.DataFrame({
    'city' : ['mumbai','delhi','pune'],
    'temperature' : [32,45,30]
})
print (temperature_df)
print ('')

windspeed_df = pd.DataFrame({
    'city' : ['mumbai','delhi','pune'],
    'windspeed' : [7,12,9]
})
print (windspeed_df)
print ('')

df = pd.concat ([temperature_df, windspeed_df], axis=1)   #appends the 2nd DF as column
print (df)
print ('')