class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        maxx = 0
        for i in sentences:
            s = len(i.split(' '))
            if s > maxx:
                maxx = s

        return maxx

