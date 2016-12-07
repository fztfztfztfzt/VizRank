import csv
import numpy as np
import matplotlib.pyplot as plt

def main():
    data,data_class = get_data()
    KNN(data,data_class)
    #print data
    #print len(data)
    #print data_class
    #print len(data_class)
    return

def KNN(data,data_class):
    numSamples = len(data_class)
    K = int(numSamples**0.5)
    attr = len(data[0])
    result = np.zeros(attr**2)
    squaredDist = np.zeros(numSamples)

    for i in xrange(numSamples):
        diff = np.tile(data[i],(numSamples,1)) - data
        squaredDiff = diff ** 2
        for n in xrange(attr-1):
            for m in xrange(n+1,attr):
                for j in xrange(numSamples):
                    squaredDist[j] = squaredDiff[j][n]+squaredDiff[j][m]
                sortedDistIndices = np.argsort(squaredDist)
                classCount = {}
                for j in xrange(1,K+1):
                    vote = data_class[sortedDistIndices[j]]
                    weight = np.exp(-squaredDist[sortedDistIndices[j]])
                    classCount[vote] = classCount.get(vote,0)+weight
                maxCount = 0
                for key,value in classCount.items():
                    if value > maxCount:
                        maxCount = value
                        maxIndex = key
                if maxIndex==data_class[i]:
                    result[n*attr+m] += 1
    #print result
    r = np.argsort(-result)
    #print r
    rr = []
    for i in range(attr*(attr-1)/2):
        rr.append([r[i]/attr+1,r[i]%attr+1])
    print rr
    draw(rr,data,data_class)
    return

def draw(rr,data,data_class):
    d = [0,1,2,len(rr)-3,len(rr)-2,len(rr)-1]
    color = ['red','blue','green']
    for j in xrange(6):
        nx = rr[d[j]][0]
        ny = rr[d[j]][1]
        x = data[:,nx-1]
        y = data[:,ny-1]
        plt.subplot('23'+str(j+1))
        for i in xrange(len(x)):
            i_class = data_class[i]-1
            plt.scatter(x[i],y[i],c=color[i_class],alpha=0.6,edgecolors='white')
        plt.xlabel('A'+str(nx))
        plt.ylabel('A'+str(ny))
        plt.grid(True)
    plt.show()


def get_data():
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
    return data,data_class

if __name__ == '__main__':
    main()
