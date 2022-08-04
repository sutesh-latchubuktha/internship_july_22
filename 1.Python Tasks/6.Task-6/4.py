import numpy
def printConcatenation(arr1,arr2):
    ndarray1 = numpy.array(arr1)
    ndarray2 = numpy.array(arr2)
    result = numpy.concatenate((arr1,arr2),axis = 0)
    print(result)
n,m,p = list(map(int,input().split()))
arr1 = []
arr2 = []
for i in range(n):
    row = list(map(int,input().split()))
    arr1.append(row)
for i in range(m):
    row = list(map(int,input().split()))
    arr2.append(row)
printConcatenation(arr1,arr2)

