import pandas as pd
import numpy as np
import operator

dataset = pd.read_csv("Customer.csv")
print(dataset)


def E_Distance(x1, x2, length):
    distance = 0

    for x in range(length):
        distance += np.square(x1[x] - x2[x])
    return np.sqrt(distance)


def knn(trainingSet, testInstance, k):
    distances = {}
    length = testInstance.shape[1]

    for x in range(len(trainingSet)):
        dist = E_Distance(testInstance, trainingSet.iloc[x], length)
        distances[x] = dist[0]
    sortdist = sorted(distances.items(), key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(sortdist[x][0])

    Count = {}
    for x in range(len(neighbors)):
        response = trainingSet.iloc[neighbors[x]][3]
        if response in Count:
            Count[response] += 1
        else:
            Count[response] = 1
    sortcount = sorted(Count.items(), key=operator.itemgetter(1), reverse=True)
    print(sortcount)
    return (sortcount[0][0], neighbors)


testSet = [[54, 25, 3],[34, 45, 2],[23, 90, 3]]
test = pd.DataFrame(testSet)
k1 = 3
result1, neigh1 = knn(dataset, test, k1)
print(neigh1)
print(result1)
