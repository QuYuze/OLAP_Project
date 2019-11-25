import pandas as pd
import numpy as np



df = pd.read_csv('Car_Sales_Data_Set.csv', header=0)

#print first 5 lines
print(df.head(5))

#group by country
grouped = df.groupby('Country')

for name, group in grouped:
    print (name)
    print (group)

#get a certain group
print (grouped.get_group('Canada'))

#get aggragate sales unit
print (grouped['Sales_Units'].agg(np.sum))

#group by country and car brand
secondGroup = df.groupby(['Country', 'Time_Year', 'Time_Quarter'])

for name, group in secondGroup:
  print (name)
  print (group)





