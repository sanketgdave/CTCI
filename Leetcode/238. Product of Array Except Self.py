class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        ans = [1]* length
        l= 1
        for i in range(length):
            ans[i] = l
            l *= nums[i]
        r= 1    
        for i in range(length-1,-1,-1):
            ans[i] *= r
            r *= nums[i]
 
        return ans