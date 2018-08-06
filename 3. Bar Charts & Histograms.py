import matplotlib.pyplot as plt

x1=[2,4,6,8,10]
y1=[6,7,8,2,4]

x2=[1,3,5,7,9]
y2=[7,8,2,4,1]

#Bar Chart
plt.bar(x1,y1,label='Bars1')
plt.bar(x2,y2,label='Bars2')

#Histogram
##ages=[22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,80,75,65,54,44,43,42,48]
##bins=[0,10,20,30,40,50,60,70,80,90,100,110,120,130] #for 0 will contain value from 0-9
##plt.hist(ages,bins,histtype='bar',rwidth=0.8)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Interesting Graph\nCheck it out')
plt.legend() #this one too for legend
plt.show()
