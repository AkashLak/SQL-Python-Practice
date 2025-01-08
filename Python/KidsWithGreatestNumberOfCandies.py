class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        new_candies = []
        max_candies = max(candies)
        bool_items = []
        for i in range(len(candies)):
            kid_new = candies[i] + extraCandies
            if kid_new >= max_candies:
                bool_items.append(True)
            else:
                bool_items.append(False)
        return bool_items
