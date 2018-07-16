# Given an integer, write a function to determine if it is a power of three.

# Example 1:

# Input: 27
# Output: true
# Example 2:

# Input: 0
# Output: false
# Example 3:

# Input: 9
# Output: true
# Example 4:

# Input: 45
# Output: false
# Follow up:
# Could you do it without using any loop / recursion?

def isPowerOfThree(num):
    count = 1
    while True:
        if count == num:
            return True
        elif count > num:
            break
        else:
            count *= 3

    return False
print(isPowerOfThree(27))
print(isPowerOfThree(0))
print(isPowerOfThree(9))
print(isPowerOfThree(45))

