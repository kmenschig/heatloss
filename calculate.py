#!/usr/bin/python3
import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

currentDirectory = os.getcwd()
print(currentDirectory)

listFile = open(currentDirectory + '/list.txt', 'r')

for line in listFile:
    inputFile = line.rstrip('\n')
#    print(inputFile)
    with open(currentDirectory + '/' + inputFile, 'r') as dataFile:
        i=0
        temperatureItem=0.0
        for line in dataFile.readlines()[2:]:
            array = line.split(',')
#            print(array[8],float(array[8]))
            if float(array[8]) >= 0.0254 and float(array[8]) <= 0.316:
                i+=1
                temperatureItem = temperatureItem + float(array[3])
                print(temperatureItem)

#        df=pd.read_csv(dataFile)
#        if str(df[df.columns[8:9]])>0.0254:
#            print(df[df.columns[3:4]])

listFile.close()

def test_function():
    pass
