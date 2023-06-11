"""
Given an integer array nums, 
return all the triplets [nums[i], nums[j], nums[k]] 
such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        triples = set()
        length = len(nums)

        for i in range(length):
            firstTriple = nums[i]
            p = {}
            for j in range(i+1, length):
                curr = nums[j]
                if -curr in p:
                    l = (list(p[-curr]) + [curr])
                    l.sort()
                    triples.add(tuple(l))
                p[firstTriple + curr] = (firstTriple, curr)
        
        return [list(x) for x in triples]


solution = Solution()
s1 = [-1,0,1,2,-1,-4] # [[-1,-1,2],[-1,0,1]]
s2 = [0,1,1]          # []
s3 = [0,0,0]          # [[0,0,0]]

sArr = [s1,s2,s3]
for s in sArr:
    print(solution.threeSum(s))