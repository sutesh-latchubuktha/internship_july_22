class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sum = 0 
        product =1
        while n >0 :
            r = n % 10 
            n = n // 10
            sum += r 
            product *= r 
        result = product - sum 
        return result
        