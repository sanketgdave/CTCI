class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = dict()

        for word in strs:
            sorted_words = tuple(sorted(word))
            if sorted_words in d: 
                d[sorted_words].append(word)
            else:
                d[sorted_words] = [word]

        return list(d.values())