# Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for x in range(0,len(haystack)):
            ans = True
            for y in range(0,len(needle)):
                if haystack[x] != needle[y]:
                    ans = False
            if ans == True:
                return x
        return -1

obj = Solution()
haystack = 'hello'
needle = 'll'
print(obj.strStr(haystack, needle))
haystack = 'aaaaa'
needle = 'bba'
print(obj.strStr(haystack, needle))
