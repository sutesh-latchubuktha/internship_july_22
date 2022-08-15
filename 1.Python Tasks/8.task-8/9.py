from statistics import mean
from operator import itemgetter
   
def lr(ar,p):
    x = list( map(itemgetter(0),ar))
    y = list( map(itemgetter(1),ar))
    xy = list(map(lambda a,b: a*b, x,y))
    x2 = list(map(lambda a: a**2,x))
    m = (mean(x)*mean(y) - mean(xy))/(((mean(x))**2) - mean(x2))
    c = mean(y) - m*mean(x)
    result = m*p + c
    return result

ar = []
for i in range(5):
    a = list(map(int, input().split()))
    ar.append(a)
p = 80
print(format(lr(ar,p),'.3f'))