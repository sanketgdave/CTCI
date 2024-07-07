class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        cnt = 0
        maxx = 0
        for char in s:
            if char == "(":
                cnt+=1
                maxx = max(cnt,maxx)
            elif char == ")":
                cnt-=1
        return maxx
