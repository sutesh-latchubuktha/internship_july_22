import numpy
numpy.set_printoptions(legacy = '1.13')
n,m = list(map(int,input().split()))
ndarray = numpy.eye(n,m)
print(ndarray)
