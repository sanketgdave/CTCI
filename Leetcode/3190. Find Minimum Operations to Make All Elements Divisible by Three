class Solution(object):
    def minimumOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        op_cnt = 0

        for num in nums:
            if num%3==0: 
                continue
            else:
                if (num-1)%3 == 0:
                    op_cnt+=1
                if (num+1)%3 == 0:
                    op_cnt+=1

        return op_cnt