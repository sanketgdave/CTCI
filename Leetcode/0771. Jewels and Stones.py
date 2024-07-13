class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewels_set = set(jewels) 
        cnt = 0
        for char in range(len(stones)):
            if stones[char] in jewels:
                cnt += 1
        return cnt
        