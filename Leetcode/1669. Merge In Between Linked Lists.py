# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        # start of list2 is the next of node before a
        # iterate through list 1 to find a
        # merge list 2 on back of a
        # end of list2 is pointed to next of b
        current = list1
        pos = 0

        while pos < a-1:
            current = current.next
            pos += 1
        prev_a = current
  
        while pos < b:
            current = current.next
            pos += 1
        post_b = current.next

        end_of_list2 = list2
        while end_of_list2.next:
            end_of_list2 = end_of_list2.next
        end_of_list2.next = post_b

        prev_a.next = list2

        return list1