class Solution(object):
    def maxProductDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # product difference between 2 pairs (a,b) and (c,d) --> (a*b) - (c*d)
        # from array nums
        # sort the array
        # take first 2 items and last 2 items
        # multiply them
        # check difference 

        nums = sorted(nums)

        return (nums[-2] * nums[-1]) - (nums[0] * nums[1])