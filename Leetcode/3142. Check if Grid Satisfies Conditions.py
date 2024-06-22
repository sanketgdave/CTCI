class Solution(object):
    def satisfiesConditions(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        rows = len(grid)
        cols = len(grid[0]) if rows > 0 else 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i + 1 < rows and grid[i][j] != grid[i + 1][j]:
                    return False
                if j + 1 < cols and grid[i][j] == grid[i][j + 1]:
                    return False

            return True


        

