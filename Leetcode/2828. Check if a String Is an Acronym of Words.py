class Solution(object):
    def isAcronym(self, words, s):
        """
        :type words: List[str]
        :type s: str
        :rtype: bool
        """
        string = ''
        # iterate through the words in the array and add it to a string
        for word in words:
            string = string + word[:1]

        # compare both strings
        if string == s:
            return True
        
        return False
        