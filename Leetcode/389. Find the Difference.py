class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        aski = [0] * 128
        
        for char in t:
            aski[ord(char)] += 1
        
        for char in s:
            aski[ord(char)] -= 1
        
        for i in range(len(aski)):
            if aski[i] == 1:
                return chr(i)
            else:
                pass
        
        return 0

# optimized

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        
        if s == t[:-1]:
            return t[-1]

        for i in range(min(len(s),len(t))):
            if s[i] == t[i]:
                pass
            else:
                return t[i]
        return

        


        