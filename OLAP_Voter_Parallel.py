import pandas as pd
import numpy as np
import threading
import time

start = time.time()

lock = threading.Lock()

def sumUp(df):
    print('Aggragated Sum: ',  df['COUNT(V.ID)'].agg(np.sum))
    print('Average: ', df['COUNT(V.ID)'].agg(np.mean))
    print('Standard Deviation: ', df['COUNT(V.ID)'].agg(np.std))

def run_thread(df):
        lock.acquire()
        try:
            sumUp(df)
        finally:
            lock.release()

df = pd.read_csv('Voter_Registration_Data.csv', header=0)
group1 = df
group2 = df.groupby('COUNTY')
group3 = df.groupby('HD_CODE')
group4 = df.groupby('PARTY')
group5 = df.groupby(['COUNTY', 'HD_CODE'])
group6 = df.groupby(['COUNTY', 'PARTY'])
group7 = df.groupby(['HD_CODE', 'PARTY'])
group8 = df.groupby(['COUNTY', 'HD_CODE', 'PARTY'])

t1 = threading.Thread(target=run_thread, args=(group1,))
t2 = threading.Thread(target=run_thread, args=(group2,))
t3 = threading.Thread(target=run_thread, args=(group3,))
t4 = threading.Thread(target=run_thread, args=(group4,))
t5 = threading.Thread(target=run_thread, args=(group5,))
t6 = threading.Thread(target=run_thread, args=(group6,))
t7 = threading.Thread(target=run_thread, args=(group7,))
t8 = threading.Thread(target=run_thread, args=(group8,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()

end = time.time()
print(end-start)