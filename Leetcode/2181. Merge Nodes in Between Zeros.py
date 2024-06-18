# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        current = head.next
        now = head
        while current:
            if current.val != 0:
                now.val += current.val
            else:
                if current.next:
                    now.next = current
                    now = current
                    now.val = 0 
            current = current.next
        now.next = None 
        return head 