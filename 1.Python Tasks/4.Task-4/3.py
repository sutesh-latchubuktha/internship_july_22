class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        combined_xor = 0
        for i in nums:
            combined_xor ^= i
        partition = combined_xor & -combined_xor
        num1 = 0
        num2 = 0
        for i in nums:
            if (i &  partition) > 0:
                num1 ^= i
            elif (i & partition) == 0:
                num2 ^= i
        return [num1,num2]
        
        