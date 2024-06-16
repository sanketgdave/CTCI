class Solution(object):
    def reversePrefix(self, word, ch):
        """
        :type word: str
        :type ch: str
        :rtype: str
        """
        pos = 0
        if ch not in word:
            return word
        for i in range(len(word)):
            if word[i] == ch:
                pos = i+1
                return word[pos-1::-1]+word[pos:]