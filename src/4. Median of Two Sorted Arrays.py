# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# Example 1:
# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:
# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        sumLen = len(nums1) + len(nums2)
        nums3 = []
        for x in range(0,sumLen):
            # print(x)
            if len(nums1)==0:
                # print('debug: 1, append - '+str(nums2[0]))
                nums3.append(nums2[0])
            elif len(nums2)==0:
                # print('debug: 2, append - '+str(nums1[0]))
                nums3.append(nums1[0])
            elif nums1[0]<nums2[0]:
                # print('debug: 3, append - '+str(nums1[0]))
                nums3.append(nums1[0])
                del nums1[0]
            else:
                # print('debug: 4, append - '+str(nums2[0]))
                nums3.append(nums2[0])
                del nums2[0]

        if sumLen%2==0:
            median = (nums3[int(sumLen/2-1)]+nums3[int(sumLen/2)])/2
        else:
            median = nums3[int(sumLen/2)]
        print(nums3)
        print(median)




nums1 = [1,2]
nums2 = [3,4]
obj = Solution()
obj.findMedianSortedArrays(nums1, nums2)