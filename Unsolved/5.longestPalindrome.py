class Solution(object):
    def longestPalindromeHelper(self, s, arr):
        """
        :type s: str
        :rtype: str
        """
        maxLen = 0
        n = len(s)
        start = 0

        for i in range(n):
            # odd
            l, r = i,i 
            while l >=0 and r < n and s[l] == s[r]:
                currLen = r - l + 1
                if currLen > maxLen:
                    maxLen = currLen
                    start = l
                l -=1
                r += 1

            # even
            l, r = i,i+1 
            while l >=0 and r < n and s[l] == s[r]:
                currLen = r - l + 1
                if currLen > maxLen:
                    maxLen = currLen
                    start = l
                l -=1
                r += 1

        return (start, maxLen)

    def longestPalindrome(self, s):
        n = len(s)
        l = [[0 for x in range(n)] for y in range(n)]
        (start, maxLen) = self.longestPalindromeHelper(s, l) 
        return s[start:start+maxLen]



# tests 
solution = Solution()
print(solution.longestPalindrome("babad")) # "bab"
print(solution.longestPalindrome("cbbd"))  # "bb"
print(solution.longestPalindrome("babab")) # "babab"