class Solution(object):
    def sumOddLengthSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # generate subarrays
        total_sum = 0
        subarrays = []
        for i in range(len(arr)):
            for j in range(i+1, len(arr) + 1):
                subarrays.append(arr[i:j])
        
        # sum the elements of odd length arrays
        for array in subarrays:
            if len(array) %2 != 0:
                total_sum += sum(array)

        return total_sum