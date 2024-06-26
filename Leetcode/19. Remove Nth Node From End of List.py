# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # First, we need to find the length of the linked list
        lcurrent = head
        length = 0
        while lcurrent:
            length += 1
            lcurrent = lcurrent.next
        print(length)  # This is for debugging purposes, can be removed
        
        # Special case: if we need to remove the head
        if n == length:
            return head.next
        
        # Find the node just before the one we need to remove
        current = head
        for _ in range(length - n - 1):
            current = current.next
        
        # Remove the N-th node from the end
        current.next = current.next.next
        
        return head