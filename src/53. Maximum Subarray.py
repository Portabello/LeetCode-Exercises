class Solution:
    def maxSubArray(self, nums):
        maxLen = None
        for subarray_len in range(1,len(nums)+1):
            for x in range(0, len(nums)):
                if maxLen == None:
                    maxLen = sum(nums[x:x+subarray_len])
                elif sum(nums[x:x+subarray_len]) > maxLen:
                    maxLen = sum(nums[x:x+subarray_len])
        return maxLen

obj = Solution()
obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
