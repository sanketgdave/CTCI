class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        s = ''
        i = 0
        while i < len(command):
            if command[i] == 'G':
                i += 1
                s += 'G'
            elif command[i] == '(':
                if command[i+1] == ')':
                    i += 2
                    s += 'o'
                elif command[i+1] == 'a' and command[i+2] == 'l' and command[i+3] == ')':
                    i += 4
                    s += 'al'
        return s

