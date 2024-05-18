class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        num = 0
        for i in range(len(nums)):
            num = num + nums[i]
            result.append(num)

        return result