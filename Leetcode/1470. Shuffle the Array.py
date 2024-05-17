class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        l = len(nums)
        new = []
        for i in range(l/2):
            new.append(nums[i])
            new.append(nums[i+n])

        return new