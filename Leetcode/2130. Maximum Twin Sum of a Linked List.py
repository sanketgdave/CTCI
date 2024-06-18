# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        current = head
        lst = []

        # convert linked_list to list
        while current:
            lst.append(current.val)
            current = current.next

        length = len(lst)
        # do the operation in list
        for item in range(length):
            if item < (length/2):
                lst[item] += lst[length - 1 - item]
        
        return max(lst)

        return