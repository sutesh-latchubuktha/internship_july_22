import numpy
def printFlatten(arr):
    ndarray = numpy.array(arr).flatten()
    print(ndarray)
def printTranspose(arr):
    ndarray = numpy.array(arr).transpose()
    print(ndarray)
    printFlatten(arr)
    

n,m = list(map(int,input().split()))
arr = []
for i in range(n):
    row = list(map(int,input().split()))
    arr.append(row)
printTranspose(arr)
