class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        # to find ascii values ord(c)
        # iterate through the string until the last characters
        # absolute difference of each adjacent characters
        # return sum of those difference 
        sum = 0
        for i in range(1,len(s)):
            sum += abs(ord(s[i-1]) - ord(s[i]))
        return sum