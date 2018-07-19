# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4



class Solution:
    def mergeTwoLists(self, l1, l2):
        ans = []
        for x in range(0, len(l1)+len(l2)):
            if len(l1) == 0:
                ans.append(l2[0])
            elif len(l2) == 0:
                ans.append(l1[0])
            elif l1[0] <= l2[0]:
                ans.append(l1[0])
                del l1[0]
            elif l2[0] <= l1[0]:
                ans.append(l2[0])
                del l2[0]
        print(ans)
l1 = [1,2,4]
l2 = [1,3,4]
obj = Solution()
obj.mergeTwoLists(l1, l2)