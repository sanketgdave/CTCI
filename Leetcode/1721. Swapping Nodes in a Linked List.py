# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        n = 0
        current = head
        while current:
            n += 1
            current = current.next
        
        pos = 0
        temp1 = 0
        temp2 = 0
        current = head
        while current:
            pos += 1
            if pos == k:
                temp1 = current.val
            if pos == n-k+1:
                temp2 = current.val

            current = current.next

        pos=0
        current = head
        while current:
            pos += 1
            if pos == k:
                current.val = temp2
            if pos == n-k+1:
                current.val = temp1
            current = current.next

        return head
