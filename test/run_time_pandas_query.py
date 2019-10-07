import pandas as pd
import time

current_time = time.clock()
@profile
def read():
    d = pd.read_csv('pandas100000.csv')

    d['ts']=pd.to_datetime(d['ts'])
    d = d.set_index(d['ts'])
    newd=d.loc['2019-10-01 00:00:00':'2019-12-01 00:00:00']
read()
print('Total inserting cost: %.6f s' % (time.clock() - current_time))
