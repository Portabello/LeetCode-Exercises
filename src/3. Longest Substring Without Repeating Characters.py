# Given a string, find the length of the longest substring without repeating characters.

# Examples:

# Given "abcabcbb", the answer is "abc", which the length is 3.

# Given "bbbbb", the answer is "b", with the length of 1.

# Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = str(s[0])
        lenAns = (len(ans))
        for x in range(0,len(s)):
            substr = s[x]
            index = ord(s[x])
            for y in range(x+1,len(s)):
                if self.compareArray(substr, s[y]) == True:
                    print(str(x)+' , '+str(y))
                    substr = substr+s[y]
                    print(substr)
                    if len(substr)>lenAns:
                        print('UPDATE')
                        ans = substr
                        lenAns = len(substr)
                else:
                    break
        print('FINAL ANSWER: '+ans)
    def compareArray(self, s, c):
        for x in range(0,len(s)):
            if ord(s[x]) == ord(c):
                return False
        return True


obj = Solution()
s = 'pwwkew'
obj.lengthOfLongestSubstring(s)