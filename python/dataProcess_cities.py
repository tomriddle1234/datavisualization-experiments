#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import collections
import os
import git
import shutil


table = []
cityNames = []
outputTable = []

def loadcsv(filename):
    """
    load prepared csv file
    """
    result = []
    with open(filename,'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=',')      
        for row in csvreader:
            result.append(row)
        #remove first row
        del result[0]
    return result 
        
def writecsv(data, filename):
    """
    write output csvfile
    data is a dict
    """
    with open(filename,'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(["ID","title","d1","d2","d3","d4","d5","news_paper"])
        for row in data:
            csvwriter.writerow(row)    

if __name__ == "__main__":
    
    table = loadcsv('all_places_refine.csv')
    cityNames = loadcsv('cityNames.csv')
#    for name_row in cityNames:
#        print name_row[0]
    
    #start process
    for row in table:
        outputRow = []
        if row[13] != "none":
            #split places in to a list
            citylist = row[13].strip().split('-')
            
            
            for i in range(5 - len(citylist)):
                citylist.append(None)
            
            #replace chinese name with english name
            for i in range(len(citylist)):
                    
                if citylist[i] != None :
                    citylist[i] = citylist[i].strip().replace(' ','')
                    
                    
                    for name_row in cityNames:
                        
                        if name_row[0].strip() == citylist[i]:
                        
                            citylist[i] = name_row[1] 
                        
#                        if name_row[0].strip() == "北京":
#                            print citylist[i]
#                            
                            
            
            outputRow = [row[0].strip(), row[5].strip(), citylist[0], citylist[1],citylist[2],citylist[3],citylist[4], row[14].strip()]
            outputTable.append(outputRow) ;
    
    
    writecsv(outputTable,'all_linked_places.csv')
    
    
    
    
    
    
    
    
