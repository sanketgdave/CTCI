class Solution(object):
    def numberGame(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        arr = []
        nums = sorted(nums)

        for i in range(0,len(nums),2):
            A = nums[i]
            B = nums[i+1]

            arr.append(B)
            arr.append(A)

        return arr

        