class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        result = start  
        i=1
        while i < n:
            result ^= (start+2*i)
            i+=1
        
        return result