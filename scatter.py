import matplotlib.pyplot as plt
import numpy as np
import csv

data = []
data_class = []
with open('wine.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    for d in f_csv:
        temp = []
        for j in range(len(d)):
            if j==0:
                data_class.append(int(d[j]))
            else:
                temp.append(float(d[j]))
        data.append(temp)
data = np.array(data)
data_class = np.array(data_class)
#print data,data_class

nx = 3
ny = 5
color = ['red','blue','green']
x = data[:,nx-1]
y = data[:,ny-1]

for i in xrange(len(x)):
    i_class = data_class[i]-1
    plt.scatter(x[i],y[i],c=color[i_class],alpha=0.6,edgecolors='white')


plt.title('Scatter')
plt.xlabel('A'+str(nx))
plt.ylabel('A'+str(ny))
plt.legend()
plt.grid(True)
plt.show()
