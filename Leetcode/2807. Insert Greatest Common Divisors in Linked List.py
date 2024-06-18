# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertGreatestCommonDivisors(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def gcd(a,b):
            while b:
                a , b =  b, a%b
            return a

        current = head
        while current and current.next:
            num1 = current.val
            num2 = current.next.val
            gcd_value = gcd(num1,num2)

            new_node = ListNode(gcd_value)
            new_node.next = current.next
            current.next = new_node
            
            current = new_node.next

        return head
