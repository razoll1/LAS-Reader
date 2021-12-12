from matplotlib import pyplot as plt
import pandas as pd
from pylab import *
import os 

plt.style.use('seaborn')

plot_list = []
Major_list = []
path_list = []
New_Major_List = []

def fileManagement():
    #reading all folders in Major folder
    folders = os.listdir('Major Folder')

    #reading each folder
    for folder in folders:
        path = 'Major Folder/'+folder
        las_files = os.listdir(path)
        #creating path for each las file
        for las_file in las_files:
            path_1 = 'Major Folder/'+folder+'/'+las_file
            #reading las files in each folder
            with open(path_1, encoding="cp437") as f:
                for l in f:
                    if l.startswith('~A'):
                        stats= l.split()[1:]
                        break
                #appending each las file into our Major_list
                Major_list.append(pd.read_csv(f, names=stats,sep = "\s+|\t+|\s+\t+|\t+\s+", engine='python'))
        for data in Major_list:
            plt.plot(data[['GTET']], data[['GTPQH']])

        plt.title(folder)
        plt.tight_layout()
        plt.show()
        Major_list.clear()


        
fileManagement()
