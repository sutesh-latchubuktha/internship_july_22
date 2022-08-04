import numpy





arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

ndarray1 = numpy.array(arr1)
ndarray2 = numpy.array(arr2)
result1 = ndarray1.dot(ndarray2)
result2 = ndarray1.cross(ndarray2)
print(result1)
print(result2)
