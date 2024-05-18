class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        leftSum = [0]
        rightSum =[0]

        sum = 0
        for i in range(0,len(nums)-1):
            sum = sum + nums[i]
            leftSum.append(sum)

        sum = 0
        for j in range(len(nums)-1,0,-1):
            sum = sum + nums[j]
            rightSum.append(sum)
        
        rightSum = rightSum[::-1]

        for k in range(len(nums)):
            answer.append(abs(leftSum[k] - rightSum[k]))

        return answer