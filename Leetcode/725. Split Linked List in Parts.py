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
        # get length l
        temp = head
        l = 0
        while temp:
            l += 1
            temp = temp.next
        print(l)

        # calculate how many parts are needed
        part_size = l//k

        # calculate how much extra is left after part
        extra = l%k

        # sub-list initialization
        result = []
        temp = head
        for i in range(k):
            result.append(temp)

            # for the initial part sizes that are larger than the latter
            current_part_size = part_size + 1 if extra > 0 else part_size
            # decrease the extra after fitting it in the intial part sizes
            extra -= 1

            # what should each sublist consist of
            for j in range(current_part_size - 1):
                temp = temp.next

            # swap temp.next with none and temp with temp.next
            if temp:
                temp.next, temp = None, temp.next
        
        # return an array of k parts
        return result