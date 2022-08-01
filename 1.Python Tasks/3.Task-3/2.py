class Solution:
    def numTeams(self, rating: List[int]) -> int:
        res = 0
        for i in range(1, len(rating) - 1):
            less, greater = [0, 0], [0, 0]
            for j in range(i):
                if rating[j] < rating[i]:
                    less[0] += 1
                else:
                    greater[0] += 1
            
            for k in range(i+1, len(rating)):
                if rating[i] < rating[k]:
                    less[1] += 1
                else:
                    greater[1] += 1
            res += less[0] * less[1] + greater[0] * greater[1]
        return res
        