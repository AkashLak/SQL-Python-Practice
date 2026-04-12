from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Returns the k most frequent elements in the array.
        Uses bucket sort algorithm
        """
        count_element = {}
        freq = [[] for i in range(len(nums) + 1)] #list of list where if k = 6, then goes 1 to 6

        for n in nums:
            count_element[n] = 1 + count_element.get(n, 0)
        
        for n, c in count_element.items(): #getting key (number), value (count) in the list of tuples
            freq[c].append(n) #adding the numbers to the actual list based on the counts (index of list)

        res = []
        for i in range(len(freq) - 1, 0, -1): #looping from end of list to start, in reverse order
            for n in freq[i]: #looping through from end of list and adding the elements with greatest count
                res.append(n)
                if len(res) == k: #checking if result set has the same number of elements as k then returning if so
                    return res