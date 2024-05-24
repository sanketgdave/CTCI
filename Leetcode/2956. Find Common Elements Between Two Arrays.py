class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        x = dict()
        y = dict()

        # make dictionary of counts of elements present in nums1
        for i in nums1:
            if i in x:
                c = x[i]
                x[i] = c+1
            else:
                x[i] = 1
        # print(x)

        # same for nums 2
        for j in nums2:
            if j in y:
                c = y[j]
                y[j] = c+1
            else:
                y[j] = 1 
        # print(y)
    
        op_lst = []
        s1 = 0
        for each_x in x.keys():
            if each_x in y.keys():
                # print(each_y)
                s1 += x[each_x]
        op_lst.append(s1)

        s2 = 0
        for each_y in y.keys():
            if each_y in x.keys():
                # print(each_y)
                s2 += y[each_y]
        op_lst.append(s2)

        # sum their counts
        # print(op_lst)
        return op_lst