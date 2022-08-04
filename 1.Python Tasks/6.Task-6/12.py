import numpy



n = int(input())
arr1 = []
arr2 = []
for i in range(n):
    row = list(map(int,input().split()))
    arr1.append(row) 
for i in range(n):
    row = list(map(int,input().split()))
    arr2.append(row) 
ndarray1 = numpy.array(arr1)
ndarray2 = numpy.array(arr2)
result = ndarray1.dot(ndarray2)
print(result)

