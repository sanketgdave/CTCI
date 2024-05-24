class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # make subarrays of length 1 to n
        distincts = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)+1):
                x = len(set(nums[i:j]))
                y = len(nums[i:j])
                if x == y:
                    distincts += (y * y)
                else:
                    distincts += (x * x)

        return distincts