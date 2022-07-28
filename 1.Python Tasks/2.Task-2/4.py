class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0 ] * length
        for i in range(length):
            count = 0 
            for j in range(length):
                if nums[i] > nums[j] and i != j :
                    count += 1 
            result[i] = count 
        return result
                    