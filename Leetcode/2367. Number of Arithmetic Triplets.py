class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        cnt = 0
        num = 0
        
        for i in range(len(nums)):
            num = nums[i] + diff
            if num in nums:
                num += diff
                if num in nums:
                    cnt+=1
        return cnt