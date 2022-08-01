class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def generateSubSets(index,subset,subsets):
            if index >= n :
                subsets.add(tuple(subset))
                return
            generateSubSets(index+1,subset,subsets)
            subset.append(nums[index])
            generateSubSets(index+1,subset,subsets)
            subset.remove(nums[index])
            return subsets           
        result = list(generateSubSets(0,[],set()))
        result = list(map(list,result))
        result.sort()
        return result   