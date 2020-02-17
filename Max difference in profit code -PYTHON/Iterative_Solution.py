# noinspection PyPep8Naming
from itertools import combinations

def readData(filename):
    file=open(filename)
    return file

def getData(file):
    values={}
    for i in file.readlines()[0].split('\r'):
        if "/" in i:
            data=map(int,i.split("/"))
            values[data[0]]=data[1]
    return values

def maxProfit(values):
    if len(values)>=2:
        valuepair=max(combinations(values.items(),2),key=lambda x:x[1][1]-x[0][1])
    return valuepair

def writeOutput(valuepair):
    f=open('Output.txt','w+')
    f.write("Maximum Profit (Iterative solution): {} \n".format(valuepair[1][1]-valuepair[0][1]))
    f.write("Day to buy: {} \n".format(valuepair[0][0]))
    f.write("Day to sell: {}".format(valuepair[1][0]))
    f.close()

file=readData('input.txt')
values=getData(file)
valuepair=maxProfit(values)
writeOutput(valuepair)
