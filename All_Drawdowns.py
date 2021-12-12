from matplotlib import pyplot as plt
import pandas as pd
from datetime import datetime
import os 
import seaborn as sns
from parse import parse




path_list = []
Major_list = []

files = os.listdir('Major Folder')

for file in files:
    path = 'Major Folder/'+file
    las_files = os.listdir(path)
    for las_file in las_files:
        path_1 = 'Major Folder/'+file+'/'+las_file
        path_list.append(path_1)
        with open(path_1,encoding="cp437") as f:
            for l in f:
                if l.startswith('~A'):
                    stats= l.split()[1:]
                    break
            Major_list.append(pd.read_csv(f, names=stats,sep = "\s+|\t+|\s+\t+|\t+\s+", engine='python'))
         
for data in Major_list:
    plt.plot(data[['GTET']], data[['GTPQH']])

plt.xlabel('Seconds')
plt.ylabel('Pressure')
plt.show()