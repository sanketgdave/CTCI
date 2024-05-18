class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        cnt = 0
        for i in range(len(nums)):
            for j in range(i):
                if (nums[i] + nums[j]) < target:
                    cnt += 1

        return cnt
        