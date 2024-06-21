class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        return prev
    
    def removeNodes(self, head):
        if not head:
            return None
        
        # Step 1: Reverse the list
        reversed_head = self.reverseList(head)
        
        # Step 2: Iterate through the reversed list and filter nodes
        max_value = float('-inf')
        dummy = ListNode(0)
        current = dummy
        
        while reversed_head:
            if reversed_head.val >= max_value:
                max_value = reversed_head.val
                current.next = ListNode(reversed_head.val)
                current = current.next
            reversed_head = reversed_head.next
        
        # Step 3: Reverse the filtered list to restore the original order
        return self.reverseList(dummy.next)