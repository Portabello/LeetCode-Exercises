# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.

# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

# (image of phone numpad goes here...)

# Example:

# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:

# Although the above answer is in lexicographical order, your answer could be in any order you want.


# :type digits: str
# :rtype: List[str]

class Solution:
    def letterCombinations(self, digits):
        # phone number mapping going from 0-9
        phoneMap = [
            ['_']
            [],
            ['a','b','c'],
            ['d','e','f'],
            ['g','h','i'],
            ['j','k','l'],
            ['m','n','o'],
            ['p','q','r','s'],
            ['t','u','v'],
            ['w','x','y','z']
        ]
        ans = []
        for x in range(0,len(digits)):

    def appendNum(self, digit, ans):
        for x in range(0,len(ans)):
            