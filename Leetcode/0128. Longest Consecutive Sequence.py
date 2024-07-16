"""
Intution:
sort the array
check next element if exists
check if next element is greater than current element 
elif check next element is equal to current element then continue
else re-initiate count to 1
after completing the conditions store the maximum of (max_cnt,cnt) in max_cnt
return max_cnt
"""
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums  = sorted(nums)
        cnt = 1
        max_cnt = 1
        #print(sorted_nums)
        if len(nums) == 0:
            return 0
        for i in range(len(sorted_nums)):
            if i < len(nums)-1:
                if sorted_nums[i]+1 == sorted_nums[i+1]:
                    cnt += 1
                elif sorted_nums[i] == sorted_nums[i+1]:
                    continue
                else:
                    cnt = 1
            max_cnt = max(max_cnt,cnt)
            # print("i:",i," cnt:",cnt," max_cnt:",max_cnt)
            
        return max_cnt