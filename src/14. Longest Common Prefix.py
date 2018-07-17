# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        minLen = 1000
        for x in range(0,len(strs)):
            if len(strs[x])<minLen:
                minLen = len(strs[x])
        substr = ''
        for x in range(0,minLen):
            commonChar = strs[0][x]
            for y in range(1,len(strs)):
                if strs[y][x] !=  commonChar:
                    return substr
            substr = substr+commonChar
        return substr


obj = Solution()
strs = ['dog', 'dog', 'doggone']
print(obj.longestCommonPrefix(strs))