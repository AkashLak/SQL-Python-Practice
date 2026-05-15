num_ways = {1:1, 2:2}
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n in num_ways:
            return num_ways[n]
        
        num_ways[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return num_ways[n]