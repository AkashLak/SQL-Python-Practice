from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds length of longest consecutive sequence in unsorted array
        """
        #Set for O(1) lookups and only starts counting when found start of a sequence
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if (n-1) not in num_set: #check if start of sequence
                length = 0
                while (n + length) in num_set:
                    length += 1
                longest = max(length, longest)
        return longest
