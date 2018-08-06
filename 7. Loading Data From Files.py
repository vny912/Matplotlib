import matplotlib.pyplot as plt

#Method 1
'''
import csv
x=[]
y=[]

with open('example.txt','r')as f:
    plots=csv.reader(f,delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x,y,label='Loaded from file')
'''

#Method 2

import numpy as np
x,y=np.loadtxt('example.txt',delimiter=',',unpack=True)
plt.plot(x,y,label='Loaded from file')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Interesting Graph\nCheck it out')
plt.legend() #this one too for legend
plt.show()
