import numpy



n,m = list(map(int,input().split()))
arr = []
for i in range(n):
    row = list(map(int,input().split()))
    arr.append(row) 
ndarray = numpy.array(arr)
print(ndarray.mean(axis =1))
print(ndarray.var(axis = 0))
print(round(ndarray.std(),11))
