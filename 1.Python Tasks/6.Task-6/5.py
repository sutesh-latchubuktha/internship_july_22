import numpy
def printOnes(arr):
    one_ndarray = numpy.ones(arr,dtype = int)
    print(one_ndarray)
def printZeros(arr):
    zero_ndarray = numpy.zeros(arr,dtype=int)
    print(zero_ndarray)
    printOnes(arr)

arr = list(map(int,input().split()))
printZeros(arr)
