# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        temp = head
        l = 0
        while temp:
            l += 1
            temp = temp.next
        print(l)

        part_size = l//k
        extra = l%k

        result = []
        temp = head
        for i in range(k):
            result.append(temp)
            current_part_size = part_size + 1 if extra > 0 else part_size
            extra -= 1
            for j in range(current_part_size - 1):
                temp = temp.next
            if temp:
                temp.next, temp = None, temp.next
                
        return result