class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        def bits(n):
            count = 0 
            while n > 0:
                if n & 1 ==1:
                    count+=1 
                n >>= 1 
            return count
        a=[]
        for i in arr:
            value = bits(i)
            d = {i:value}
            a.append(d)
        def condition(d):
            for key in d:
                return d[key]
        a.sort(key = condition)
        result = [] 
        for i in a :
            for j in i:
                result.append(j)
        return result
            
        
        