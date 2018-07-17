# Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines
# are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis
# forms a container, such that the container contains the most water.

# Note: You may not slant the container and n is at least 2.

class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxarea = 0
        ans = [-1,-1]
        for x in range(0,len(height)):
            for y in range(x+1, len(height)):
                if self.findArea(height[x],height[y], y-x) > maxarea:
                    maxarea = self.findArea(height[x],height[y], y-x)
                    ans = [height[x], height[y]]
        print('MAXAREA = '+str(maxarea)+'| n1 = '+str(ans[0])+'| n2 = '+str(ans[1]))


    def findArea(self, n1, n2, dist):
        toparea = 0
        if n1 != n2:
            toparea = abs(n2-n1)*dist/2
        bottomarea = n1*dist if n1<n2 else n2*dist
        area = bottomarea + toparea
        return area

obj = Solution()
height = [1,3,2]
obj.maxArea(height)