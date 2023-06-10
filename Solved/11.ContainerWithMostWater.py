class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxArea = 0
        lo, hi = 0, len(height) - 1
        max_height = max(height) # upper limit for the height of any container

        while lo < hi:
            if maxArea // (hi-lo) > max_height:
                return maxArea # further iterations would not result in a larger area
            currArea = min(height[lo], height[hi]) * (hi - lo)
            maxArea = max(maxArea, currArea)
            if height[hi] > height[lo]:
                lo += 1
            elif height[lo] > height[hi]:
                hi -= 1
            else:
                if height[lo+1] > height[hi-1]:
                    lo += 1
                else:
                    hi -= 1

        return maxArea
        

solution = Solution()
print(solution.maxArea([1,1])) # 1
print(solution.maxArea([1,8,6,2,5,400,8,3,7])) # 49


