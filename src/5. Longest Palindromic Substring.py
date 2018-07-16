# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s):
        longestPalin = s[0]
        for x in range(0,len(s)):
            for y in range(x+1, len(s)):
                substr = s[x:y+1]
                if self.checkifPalindrome(substr) and len(substr)>len(longestPalin):
                    longestPalin = substr
        return longestPalin

    def checkifPalindrome(self, s):
        reversedS = s[::-1]
        for x in range(0,len(s)):
            if s[x] != reversedS[x]:
                return False
        return True

obj = Solution()
s = 'racecar'
print(obj.longestPalindrome(s))