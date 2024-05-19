class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        new_dict = {}
        keys = indices
        values = s

        # Zip the lists together and iterate
        for key, value in zip(keys, values):
            new_dict[key] = value
        
        s1 = ""
        for value in new_dict.values():
            s1+=value
        
        return s1
            