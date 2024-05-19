class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt = 0
        nums = sorted(nums)

        for i in range(len(nums)):
            if nums[i] < k:
                cnt+=1
            else:
                continue

        return cnt

        