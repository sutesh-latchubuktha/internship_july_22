import numpy
numpy.set_printoptions(legacy = '1.13')


n,m = list(map(int,input().split()))
arr = []
for i in range(n):
    row = list(map(int,input().split()))
    arr.append(row) 
ndarray = numpy.array(arr)
result = ndarray.sum(axis = 0)
output = result.prod()
print(output)
