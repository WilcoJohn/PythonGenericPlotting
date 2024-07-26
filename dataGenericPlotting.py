# -*- coding: utf-8 -*-
"""

Python code file for data analysis 
"""
import numpy
import pandas
import matplotlib.pyplot as plt
import os
import fnmatch

# interactive app stuff
# import tkinter
# m = tkinter.Tk()
# m.mainloop()





def getRelevantFilePaths(path, pattern, matchPattern = True):       # get relevant files according to a pattern
    results = [];
    for root, dirs, files in os.walk(path):
        for fi in files:
            filePathName = root + '\\' + fi;
            if (fnmatch.fnmatch(filePathName,pattern) and matchPattern):
                results.append(filePathName);                   # if pattern matches append file
                
            if (not fnmatch.fnmatch(filePathName,pattern) and not matchPattern):
                results.append(filePathName);                   # if pattern does not match, append file
        
    results.sort();
    return results;



filePath = rf"C:\Users\wilco\OneDrive - Resonant Group\Desktop\Projects\13450 - DEEP\Data Analysis";           # raw string with string interpolation
filePattern = "*2024-07-22*.csv";   # file patterns to list

relevantFilePaths = getRelevantFilePaths(filePath,filePattern);
dataRaw = pandas.read_csv(relevantFilePaths[0],skiprows=1);

dataPlot = dataRaw[['Time_min','Sensor1','Sensor2','Sensor3','Sensor4']].rolling(window = 60, 
           center = True).mean().dropna();  # do a middle moving average to filter data
                                            # and get rid of unnecesary data
                                            
                                            
F = plt.figure(figsize=(7, 4));
# ax = F.add_subplot(111)     

plt.plot(dataPlot["Time_min"],dataPlot["Sensor3"], label = "T$_{cond}$", color = '#2ca02c'); 


plt.show();                             
