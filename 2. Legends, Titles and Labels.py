import matplotlib.pyplot as plt

x1=[1,2,3]
y1=[5,7,4]

x2=[1,2,3]
y2=[10,14,12]

plt.plot(x1,y1,label='First Line') #label is for adding legend
plt.plot(x2,y2,label='Second Line')
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting Graph\nCheck it out')
plt.legend() #this one too for legend
plt.show()
