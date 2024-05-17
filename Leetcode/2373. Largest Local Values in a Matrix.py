class Solution(object):

    def findMax(self,grid,x,y):
        max_element = 0
        for i in range(x,x+3):
            for j in range(y,y+3):
                max_element = max(max_element, grid[i][j])
        return max_element

    def largestLocal(self, grid):
        n = len(grid)
        maxLocal = [[0] * (n-2) for _ in range(n-2)]
        for i in range(n-2):
            for j in range(n-2):
                maxLocal[i][j] = self.findMax(grid,i,j)
        return maxLocal