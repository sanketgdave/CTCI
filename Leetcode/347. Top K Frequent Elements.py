class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # Step 1: Count the frequency of each element using a dictionary
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Step 2: Sort the elements based on their frequencies in descending order
        # count.items() returns a list of tuples [(element, frequency), ...]
        # key=lambda x: x[1] tells sorted() to sort by the frequency part of the tuple
        # reverse=True tells sorted() to sort in descending order
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)
        
        # Step 3: Extract the top k elements from the sorted list
        # item[0] extracts the element from each tuple (element, frequency)
        top_k_elements = [item[0] for item in sorted_items[:k]]
        
        return top_k_elements