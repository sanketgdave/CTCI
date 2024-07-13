class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        largestCommonPrefix = strs[0]
        newstr = ''
                        
        for s in strs:
            for i in range(min(len(largestCommonPrefix),len(s))):
                if s[i] == largestCommonPrefix[i]:
                    newstr += s[i]
                else:
                    break

            largestCommonPrefix = newstr
            newstr = ''

        return largestCommonPrefix