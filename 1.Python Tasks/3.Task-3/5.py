class Solution:
    def countBits(self, n: int) -> List[int]:
        def countBits(number):
            count = 0 
            while number > 0 :
                if number & 1 == 1:
                    count += 1
                number >>= 1
            return count
        result = [0] * (n+1)
        for i in range(n+1):
            result[i] = countBits(i)
        return result
            
        