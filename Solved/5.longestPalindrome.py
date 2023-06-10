class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        n = len(s)
        start = 0
        maxLen = 1

        for i in range(n):
            # Odd
            l, r = i, i
            while l > 0 and r < n - 1 and s[l - 1] == s[r + 1]:
                l -= 1
                r += 1

            if r - l + 1 > maxLen:
                start = l
                maxLen = r - l + 1

            # Even
            l, r = i, i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            if r - l - 1 > maxLen:
                start = l + 1
                maxLen = r - l - 1

        return s[start:start + maxLen]





# tests 
solution = Solution()
print(solution.longestPalindrome("babad")) # "bab"
print(solution.longestPalindrome("cbbd"))  # "bb"
print(solution.longestPalindrome("babab")) # "babab"