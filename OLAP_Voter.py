import pandas as pd
import numpy as np
import time

start = time.time()
#read the data from csv file
df = pd.read_csv('Voter_Registration_Data.csv', header=0)

group1 = df
group2 = df.groupby('COUNTY')
group3 = df.groupby('HD_CODE')
group4 = df.groupby('PARTY')
group5 = df.groupby(['COUNTY', 'HD_CODE'])
group6 = df.groupby(['COUNTY', 'PARTY'])
group7 = df.groupby(['HD_CODE', 'PARTY'])
group8 = df.groupby(['COUNTY', 'HD_CODE', 'PARTY'])

print('Aggragated Sum: ', group1['COUNT(V.ID)'].agg(np.sum))
print('Average: ', group1['COUNT(V.ID)'].agg(np.mean))
print('Standard Deviation: ', group1['COUNT(V.ID)'].agg(np.std))

print('Aggragated Sum: ', group2['COUNT(V.ID)'].agg(np.sum))
print('Average: ', group2['COUNT(V.ID)'].agg(np.mean))
print('Standard Deviation: ', group2['COUNT(V.ID)'].agg(np.std))

print('Aggragated Sum: ', group3['COUNT(V.ID)'].agg(np.sum))
print('Average: ', group3['COUNT(V.ID)'].agg(np.mean))
print('Standard Deviation: ', group3['COUNT(V.ID)'].agg(np.std))

print('Aggragated Sum: ', group4['COUNT(V.ID)'].agg(np.sum))
print('Average: ', group4['COUNT(V.ID)'].agg(np.mean))
print('Standard Deviation: ', group4['COUNT(V.ID)'].agg(np.std))

print('Aggragated Sum: ', group5['COUNT(V.ID)'].agg(np.sum))
print('Average: ', group5['COUNT(V.ID)'].agg(np.mean))
print('Standard Deviation: ', group5['COUNT(V.ID)'].agg(np.std))

print('Aggragated Sum: ', group6['COUNT(V.ID)'].agg(np.sum))
print('Average: ', group6['COUNT(V.ID)'].agg(np.mean))
print('Standard Deviation: ', group6['COUNT(V.ID)'].agg(np.std))

print('Aggragated Sum: ', group7['COUNT(V.ID)'].agg(np.sum))
print('Average: ', group7['COUNT(V.ID)'].agg(np.mean))
print('Standard Deviation: ', group7['COUNT(V.ID)'].agg(np.std))

print('Aggragated Sum: ', group8['COUNT(V.ID)'].agg(np.sum))
print('Average: ', group8['COUNT(V.ID)'].agg(np.mean))
print('Standard Deviation: ', group8['COUNT(V.ID)'].agg(np.std))

end = time.time()
print(end-start)