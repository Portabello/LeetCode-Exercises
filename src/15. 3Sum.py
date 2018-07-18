# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# he solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


# :type nums: List[int]
# :rtype: List[List[int]]

class Solution:
    def threeSum(self, nums):
        ans = []
        for i in range(0,len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0 and self.checkDuplicate(ans, [nums[i], nums[j], nums[k]]) == False:
                        ans.append([nums[i], nums[j], nums[k]])
        return ans
    # definitely can improve checking algorithm here,
    def checkDuplicate(self, ans, num):
        if len(ans)==0:
            return False
        for x in range(0,len(ans)):
            temp = 0
            for y in range(0,3):
                if num[y]==ans[x][0]:
                    temp+=1
                elif num[y]==ans[x][1]:
                    temp+=1
                elif num[y]==ans[x][2]:
                    temp+=1
            if temp == 3:
                return True
            temp = 0
        return False



obj = Solution()
nums = [-1,0,1,2,-1,-4]
print('FINAL ANSWER: '+str(obj.threeSum(nums)))