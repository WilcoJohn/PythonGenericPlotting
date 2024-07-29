# -*- coding: utf-8 -*-
"""

Python code file for generic data plotting and file filtering 

"""
import numpy
import pandas
import matplotlib.pyplot as plt
import os
import fnmatch





def getRelevantFilePaths(path, pattern, matchPattern = True):       # get relevant files according to a pattern
    results = [];
    
    if (type(path) is str):
        for root, dirs, files in os.walk(path):
            for fi in files:
                filePathName = root + '\\' + fi;
                if (fnmatch.fnmatch(filePathName,pattern) and matchPattern):
                    results.append(filePathName);                   # if pattern matches append file
                
                if (not fnmatch.fnmatch(filePathName,pattern) and not matchPattern):
                    results.append(filePathName);                   # if pattern does not match, append file
    
    elif (type(path) is list or tuple):                             # filter iteratible list for relevant patter
        if (matchPattern): 
            results = fnmatch.filter(path, pattern);
        else: 
            for pi in path:
                if (not fnmatch.fnmatch(pi,pattern)):
                    results.append(pi);
    else:
        return "error";
        
    results.sort();
    return results;








filePath = r"C:\Users\Test\File\For\User";           # raw string with string interpolation
filePattern = "*.csv";                               # file patterns to list

relevantFilePaths = getRelevantFilePaths(filePath,filePattern);
dataRaw = pandas.read_csv(relevantFilePaths[0],skiprows=1);


dataPlot = dataRaw[['Time_min','Sensor1','Sensor2','Sensor3','Sensor4']].rolling(window = 60, 
           center = True).mean().dropna();  # do a middle moving average to filter data
                                            # and get rid of unnecesary data
                                            
                                            
                                            
                                            
                                            
                                            
F = plt.figure(figsize=(7, 4));
# ax = F.add_subplot(111)     

xCol = 'Time_min';
yCol = 'Sensor1';



plt.plot(dataRaw[xCol],dataRaw[yCol], label = "T$_{unfiltered}$", color = 'r'); 
plt.plot(dataPlot[xCol],dataPlot[yCol], label = "T$_{filtered}$", color = 'b'); 

vlinePlots = [60,120];

# filter values using logical array indexing/slicing
meanTempVlines = dataPlot[(dataPlot[xCol]>=numpy.min(vlinePlots)) 
                          & (dataPlot[xCol]<=numpy.max(vlinePlots))][yCol].mean();

plt.vlines(vlinePlots, 0, dataPlot[yCol].max() *1.05, linestyles = '--',
           label = "Mean value {}".format(numpy.round(meanTempVlines,2)),
           color = 'k');


plt.xlim([dataPlot[xCol].min(), dataPlot[xCol].max() *1.05]);
plt.ylim([0, dataPlot[yCol].max() *1.05]);


plt.legend(loc = [1.05,0.65]);
plt.ylabel('yVal [--]');
plt.xlabel('xVal [--]');
plt.show();                             




