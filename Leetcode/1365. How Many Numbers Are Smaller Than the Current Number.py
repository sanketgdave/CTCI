class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        sorted_nums = sorted(nums)

        for i in nums:
            num = sorted_nums.index(i)
            result.append(num)

        return result