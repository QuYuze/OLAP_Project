import pandas as pd
import numpy as np

#read the data from csv file
df = pd.read_csv('Car_Sales_Data_Set.csv', header=0)

group1 = df
group2 = df.groupby('Country')
group3 = df.groupby('Time_Year')
group4 = df.groupby(['Time_Year', 'Time_Quarter'])
group5 = df.groupby('Car_Manufacturer')
group6 = df.groupby(['Country', 'Time_Year'])
group7 = df.groupby(['Country', 'Time_Year', 'Time_Quarter'])
group8 = df.groupby(['Country', 'Car_Manufacturer'])
group9 = df.groupby(['Time_Year', 'Car_Manufacturer'])
group10 = df.groupby(['Time_Year', 'Time_Quarter', 'Car_Manufacturer'])
group11 = df.groupby(['Country', 'Time_Year', 'Car_Manufacturer'])
group12 = df.groupby(['Country', 'Time_Year', 'Time_Quarter', 'Car_Manufacturer'])

nb = input('Enter your input: '+'\n'+
'''
           1. ()	
           2. (Country)	
           3. (Time_Year)	
           4. (Time_Quarter	-Time_Year)	
           5. (Car_	Manufacturer)	
           6. (Country,	Time_Year)	
           7. (Country,	Time_Quarter-Time_Year)	
           8. (Country,	Car_Manufacturer)	
           9. (Time_Year, Car_Manufacturer)	
           10. (Time_Quarter-Time_Year,	Car_Manufacturer)	
           11. (Country, Time_Year,	Car_Manufacturer)	
           12. (Country, Time_Quarter-Time_Year, Car_Manufacturer)
''')
number = int(nb)
if number == 1:
    print(group1['Sales_Units'].agg(np.sum))
elif number == 2:
    print(group2['Sales_Units'].agg(np.sum))
elif number == 3:
    print(group3['Sales_Units'].agg(np.sum))
elif number == 4:
    print(group4['Sales_Units'].agg(np.sum))
elif number == 5:
    print(group5['Sales_Units'].agg(np.sum))
elif number == 6:
    print(group6['Sales_Units'].agg(np.sum))
elif number == 7:
    print(group7['Sales_Units'].agg(np.sum))
elif number == 8:
    print(group8['Sales_Units'].agg(np.sum))
elif number == 9:
    print(group9['Sales_Units'].agg(np.sum))
elif number == 10:
    print(group10['Sales_Units'].agg(np.sum))
elif number == 11:
    print(group11['Sales_Units'].agg(np.sum))
elif number == 12:
    print(group12['Sales_Units'].agg(np.sum))