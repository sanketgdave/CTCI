class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        maxim = 0
        
        for i in range(len(accounts)):
            s = 0
            for j in range(len(accounts[0])):
                s = s + accounts[i][j] 
            
            if s > maxim:
                maxim = s
                    
        return maxim
