class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first = 0
        second = 0
        f = 0 
        s = 0
        length = len(nums)
        for i in range(length):
            if nums[i] > first:
                first = nums[i]
                f = i 
        for i in range(length) :
            if nums[i] > second and f != i:
                second = nums[i]
                s = i 
        result = (nums[f]-1) * (nums[s]-1)
        return result