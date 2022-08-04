import numpy
def printShape(arr):
    
    ndarray = numpy.array(arr).reshape(3,3)
    print(ndarray)

arr = list(map(int,input().split()))
printShape(arr)



