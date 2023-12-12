import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripped_s = re.sub(r'\W+', '', s).lower()
        stripped_s = stripped_s.replace("_", "")
        reverse_stripped_s = stripped_s[::-1]       
        if(stripped_s == reverse_stripped_s):
            return True
        return False
