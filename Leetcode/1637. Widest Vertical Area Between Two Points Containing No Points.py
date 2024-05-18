class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        lst = []
        max_diff = 0
        
        for i in range(len(points)):
            lst.append(points[i][0])

        lst = sorted(lst)

        for j in range(len(lst)):
            if j == (len(lst)-1):
                continue
            diff = lst[j+1] - lst[j]
            if diff > max_diff:
                max_diff = diff
                
        return max_diff