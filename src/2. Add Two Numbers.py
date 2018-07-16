# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# ----------------------------------------------------------------------------------
# Definition for singly-linked list.


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1str=''
        for x in range(len(l1)-1, -1, -1):
            #print(x)
            l1str += str(l1[x])

        l2str = ''
        for x in range(len(l2)-1, -1, -1):
            l2str += str(l2[x])

        print(l1str + ' . '+l2str)
        sum = int(l1str) + int(l2str)
        print(sum)
        sumStr = str(sum)[::-1]
        ans = []
        for x in range(0,len(sumStr)):
            ans.append(sumStr[x])
        print (ans)


obj = Solution()
l1 = [2,4,3]
l2 = [5,6,4]
# print(len(l1))
obj.addTwoNumbers(l1,l2)
