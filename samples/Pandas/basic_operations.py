"""
Basic operation using pandas python library
"""
from pandas import DataFrame, read_csv

import pandas as pd
import sys
import matplotlib.pyplot as plt 
import matplotlib


print ("Python Version" + sys.version)
print ("Pandas Version" + pd.__version__)
print ("Matplotlib Version" + matplotlib.__version__)

names = ['Bob','Jessica','Mary','John','Mel']
births = [968, 155, 77, 578, 973]


babyDataSet = list(zip(names, births))
df = pd.DataFrame(data=babyDataSet, columns=["Names", "Birth"])
#print(df)

df.to_csv("births1880.csv", index=False, header=False)

csvLocation = r'./births1880.csv'
#df = pd.read_csv(csvLocation, header=None)
df = pd.read_csv(csvLocation, names=["Names", "Births"])

print (df)

# Analyse Data to find most popular name

sorted = df.sort_values(["Births"], ascending=False)
print (sorted.head(1))


# OR find the max value
maxValue = df["Births"].max()
print(maxValue)



df["Births"].plot()
maxName = df["Names"][df["Births"] == df["Births"].max()].values

txt = str(maxValue) + " - "   + maxName
plt.annotate(txt, xy=(1, maxValue), xytext=(8, 0), 
                 xycoords=('axes fraction', 'data'), textcoords='offset points')

print ("most popular name")
print(df[df['Births'] == df['Births'].max()])
plt.show()
