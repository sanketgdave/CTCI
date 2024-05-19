class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        comp=[]

        for i in range(0,len(nums),2):
            comp.append(nums[i] * [nums[i+1]])
            
        result = []
        for j in comp:
            result = result + j

        return result