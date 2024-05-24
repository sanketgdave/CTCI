class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = max(nums)
        nums.remove(x)
        y = max(nums)
        nums.remove(y)

        return ((x-1) * (y-1))