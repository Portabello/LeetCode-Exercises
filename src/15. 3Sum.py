class Solution:
    def threeSum(self, nums):
        ans = []
        for x in range(0, len(nums)):
            for y in range(x+1, len(nums)):
                for z in range(y+1, len(nums)):
                    #print('(', x, ',',y, ',',z, ')')
                    if nums[x]+nums[y]+nums[z]==0 and self.checkDuplicate(ans, [nums[x], nums[y], nums[z]]):
                        ans.append([nums[x], nums[y], nums[z]])
                        #print('[',nums[x], ',', nums[y], ',', nums[z],']')
        return ans


    def checkDuplicate(self, ans, num):
        print(num)
        if len(ans) == 0:
            return True
        for x in ans:
            copy_num = num[:]
            for i in x:
                for j in copy_num:
                    if j == i:
                        #print('removing:',j)
                        copy_num.remove(j)
                if len(copy_num) == 0:
                    return False
        return True





obj = Solution()
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
print('FINAL ANSWER: '+str(obj.threeSum(nums)))
