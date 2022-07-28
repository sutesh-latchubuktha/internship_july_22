from math import *
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        result = 0 
        for i in nums:
            result += int(log10(i)) & 1  
        return result
        
        