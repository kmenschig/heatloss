#!/usr/bin/python3
import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

currentDirectory = os.getcwd()
print(currentDirectory)

listFile = open(currentDirectory + '/list.txt', 'r')
resultFile = open(currentDirectory + '/result.csv', 'w')

for line in listFile:
    inputFile = line.rstrip('\n')
    timeItem = inputFile[1:inputFile.index('.')]
    stop=False
    with open(currentDirectory + '/' + inputFile, 'r') as dataFile:
        i=0
        temperatureItem=0.0
        for line in dataFile.readlines()[2:]:
            array = line.split(',')

            if float(array[8]) >= 0.0254 and float(array[8]) <= 0.316:
                i+=1
                temperatureItem = temperatureItem + float(array[3])

                if float(array[8]) > 0.0508 and stop==False:
                    ftim=str(temperatureItem/i)
                    fi=str(i)
                    stop=True

        temperatureItem=temperatureItem/i
        resultFile.write(timeItem + ',' + ftim + ',' + fi + ',' + str(temperatureItem) + ',' + str(i) + '\n')
                    
listFile.close()
resultFile.close()

x=[]
y1=[]
y2=[]

with open(currentDirectory + '/result.csv', 'r') as csvfile:
    plots= csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y1.append(float(row[1]))
        y2.append(float(row[3]))

plt.plot(x,y1, linewidth=0, marker='o')
plt.plot(x,y2, linewidth=0, color='red', marker='+', markersize=8)
plt.legend(('Average of 1st inch from Insulation', 'Average of Total',),loc='upper right')
plt.title('Heat Loss from Pail in Middle Vertical Direction')

plt.xlabel('Time [hr]')
plt.ylabel('Temperature [K]')

plt.show()

