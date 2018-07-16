# Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

# Example:
# Given nums = [-2, 0, 3, -5, 2, -1]

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# Note:
# You may assume that the array does not change.
# There are many calls to sumRange function.
class NumArray:
    numList = []
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.numList = nums

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        counter = 0
        for x in range(i,j+1):
            counter += self.numList[x]
        print(counter)


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
obj.sumRange(0, 2)
obj.sumRange(2, 5)
obj.sumRange(0, 5)
#param_1 = obj.sumRange(i,j)