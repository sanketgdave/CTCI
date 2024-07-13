# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode(0)  # Dummy head for the result linked list
        current = dummy  # Pointer to the current node in the result list
        carry = 0  # Variable to store carry value
        
        while l1 is not None or l2 is not None:
            x = l1.val if l1 is not None else 0
            y = l2.val if l2 is not None else 0
            total = carry + x + y
            
            carry = total // 10  # Update carry
            current.next = ListNode(total % 10)  # Create a new node with the digit part
            current = current.next  # Move to the next node
            
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
        
        if carry > 0:  # If there is any carry left at the end
            current.next = ListNode(carry)
        
        return dummy.next
        
    