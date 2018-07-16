# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.
# Example:
# Given num = 16, return true. Given num = 5, return false.
# Follow up: Could you solve it without loops/recursion?

def isPowerOfFour(num):
    count = 1
    while True:
        if count == num:
            return True
        elif count > num:
            break
        else:
            count *= 4

    return False
print(isPowerOfFour(16))
print(isPowerOfFour(5))