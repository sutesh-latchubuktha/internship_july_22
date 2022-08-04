import numpy



p = list(map(float,input().split()))
x = int(input())
ndarray1 = numpy.array(p)
result = numpy.polyval(ndarray1,x)
print(result)
