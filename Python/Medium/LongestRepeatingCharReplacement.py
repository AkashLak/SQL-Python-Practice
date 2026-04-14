class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Returns the length of the longest substring that can be obtained
        by replacing at most k characters
        """
        #Dict that stores freq of characters in current window
        count = {}
        #Left pointer of sliding window
        l = 0
        #Stores max valid window length
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
