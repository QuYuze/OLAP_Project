import pandas as pd
import numpy as np
import itertools
import time

start = time.time()
df = pd.read_csv('Voter_Registration_Data.csv')

titile = ['COUNTY', 'HD_CODE', 'HD_NAME', 'CD_CODE', 'CD_NAME', 'PARTY', 'SYSDATE']
combi = []
#index = 1
for num in range(1, len(titile)+1):
    combi += itertools.combinations(titile, num)
'''for option in combi:
    print('(' + str(index) + ')' + str(option))
    index += 1'''

#inp = input('Enter the command: ')
#while inp != 'q':
#command = int(inp)
for command in range(0, len(combi)):
    #command = command - 1
    value = combi[command]
    grouped = df.groupby(value)
    print(grouped['COUNT(V.ID)'].agg(np.sum))
    #inp = input('Enter another command to continue(enter \'q\' to exit): ')
end = time.time()
print(end - start)
'''elif command == 0:
    print('Total Voter Count: ' + str(df['COUNT(V.ID)'].agg(np.sum)))
    inp = input('Enter another command to continue(enter \'q\' to exit): ')'''