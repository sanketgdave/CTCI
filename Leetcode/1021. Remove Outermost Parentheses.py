class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        cnt = 0
        substrs = ''
        lst = []

        for char in s:
            cnt+=1 if char == '(' else 0
            cnt-=1 if char == ')' else 0
            substrs += char
            if cnt == 0:
                lst.append(substrs)
                substrs = ''
                continue

        for s in lst: 
            for i in range(1,len(s)-1):
                stack.append(s[i])
        
        return ''.join(stack)
