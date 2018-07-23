# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.

# Example 1:

# Input: "()"
# Output: true
# Example 2:

# Input: "()[]{}"
# Output: true
# Example 3:

# Input: "(]"
# Output: false
# Example 4:

# Input: "([)]"
# Output: false
# Example 5:

# Input: "{[]}"
# Output: true

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for x in range(0,len(s)):
            if s[x] == ')':
                if stack[len(stack)-1] == '(':
                    stack.pop()
                else:
                    return False
            elif s[x] == ']':
                if stack[len(stack)-1] == '[':
                    stack.pop()
                else:
                    return False
            elif s[x] == '}':
                if stack[len(stack)-1] == '{':
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[x])
        if len(stack)==0:
            return True
        return False

obj = Solution()
s = '()'
print(s)
print(obj.isValid(s))
s = '()[]{}'
print(s)
print(obj.isValid(s))
s = '(]'
print(s)
print(obj.isValid(s))
s = '([)]'
print(s)
print(obj.isValid(s))
s = '{[]}'
print(s)
print(obj.isValid(s))
