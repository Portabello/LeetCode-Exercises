# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Note:

# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        ans  = 0
        negative = False
        if divisor<0 or dividend<0:
            if divisor<0 and dividend<0:
                negative = False
            else:
                negative = True

        while abs(dividend) > 0:
            if abs(dividend)-abs(divisor) > 0:
                dividend = abs(dividend) - abs(divisor)
                ans += 1
            else:
                break
        if negative == True:
            ans = ans - 2*ans
        return ans
obj = Solution()
dividend = 10
divisor = 3
print(obj.divide(dividend, divisor))
dividend = 7
divisor = -3
print(obj.divide(dividend, divisor))