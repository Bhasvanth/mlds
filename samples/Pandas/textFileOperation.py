"""
    This module is used to get hands-on experience with PANDAS module.
    
"""


import pandas as pd
from numpy import random
import matplotlib.pyplot as plt
import sys
import matplotlib


names=['Bob','Jessica','Mary','John','Mel']

def generateDataSet(filename):
    try :
        random.seed(500)
        random_names = [ names[random.randint(low=0, high=len(names))] for i in range(1000)]
        print(random_names[:10])


        births = [random.randint(low=0, high=1000) for i in range(1000)]
        print (births[:10])

        babyDataSet = list(zip(random_names, births))
        print(babyDataSet[:10])


        df = pd.DataFrame(data=babyDataSet, columns=["Names", "Births"])
        print(df[:10])

        df.to_csv(filename, index=False,header=False)
        return filename
    except Exception as e:
        print (str(e))
        return False



def readDataSet(filename):
    try :
        df = pd.read_csv(filename, names=["Names", "Births"])
        #print(df.info())
        #print(df.head(10))
        #print(df.tail())
        name = df.groupby("Names")
        df = name.sum()
        Sorted = df.sort_values(["Births"], ascending=False)
        maxValue = Sorted.head(1)
        return Sorted
    except Exception as e:
        print (str(e))
        return False

def plotDataSet(df):
    try:
        print ("Most Popular Name")
        print (df)
        df["Births"].plot.bar()
    except Exception as e:
        print(str(e))
        return False
if __name__ == "__main__":
    generateDataSet("testFileOperations.txt")
    df = readDataSet("testFileOperations.txt")
    if df is not False:
        plotDataSet(df)
 
