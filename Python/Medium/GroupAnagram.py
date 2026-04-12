from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups strings that are anagrams of each other
        """
        
        #Approach #1 (sort each string and use as key)
        #Slower since O(klog(k)) per string
        """result = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            result[sorted_s].append(s)
        
        return list(result.values())"""

        #Approach 2 (use character count array (O(k)) as unique signature for each anagram group)

        result = defaultdict(list) #mapping charCount to list of anagrams

        for s in strs:
            count = [0] * 26

            for char in s:
                count[ord(char) - ord("a")] += 1
                
            result[tuple(count)].append(s)

        return list(result.values())