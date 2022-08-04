import numpy
import numpy.linalg as algebra



n = int(input())
arr = []
for i in range(n):
    row = list(map(float,input().split()))
    arr.append(row)
ndarray = numpy.array(arr)
result = algebra.det(ndarray)
print(round(result,2))
