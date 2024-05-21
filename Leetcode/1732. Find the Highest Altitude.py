class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        alt_sum = 0
        max = 0
        
        # for each element in gain 
        # sum it with the previous element in altitude 
        # and store it in altitude

        for i in gain:
            alt_sum += i
            if alt_sum > max:
                max = alt_sum
            
        return max
            