import numpy
numpy.set_printoptions(legacy = '1.13')


arr = list(map(float,input().split()))
ndarray = numpy.array(arr)
print(numpy.floor(ndarray))
print(numpy.ceil(ndarray))
print(numpy.rint(ndarray))
