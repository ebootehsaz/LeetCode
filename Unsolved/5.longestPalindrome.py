class Solution(object):
    def longestPalindromeHelper(self, s, arr):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 0
        n = len(s)

        for i in range(n):
            # odd
            l, r = i,i 
            while l >=0 and r < n and s[l] == s[r]:
                currLen = r - l + 1
                maxLen = max(currLen, maxLen)
                l -=1
                r += 1

            # even
            l, r = i,i+1 
            while l >=0 and r < n and s[l] == s[r]:
                currLen = r - l + 1
                maxLen = max(currLen, maxLen)
                l -=1
                r += 1

        return maxLen

            



    def longestPalindrome(self, s):
        n = len(s)
        l = [[0 for x in range(n)] for y in range(n)]
        return self.longestPalindromeHelper(s, l) 



# tests 
solution = Solution()
print(solution.longestPalindrome("babad")) # "bab"
print(solution.longestPalindrome("cbbd"))  # "bb"

"""
palindrome("") = T 

"""