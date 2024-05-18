class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        lst = [False] * len(candies)
        mx = max(candies)
        
        for i in range(len(candies)):
            if  mx <= (candies[i] + extraCandies):
                lst[i] = True
        
        return lst