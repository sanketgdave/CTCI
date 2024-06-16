class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        res = ''
        for i in range(len(address)):
            if address[i] == '.':
                res += '[.]'
            else:
                res += address[i]
        return res

        