class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        int_num = 0
        new_value = 0
        prev_value = 0
        roman_to_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        for roman in reversed(s):
            new_value = roman_to_int[roman]
            if new_value >= prev_value:
                int_num = int_num + new_value
                prev_value = new_value
            else:
                int_num = int_num - new_value
                prev_value = new_value
        
        return int_num
