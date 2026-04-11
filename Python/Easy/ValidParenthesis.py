class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        paren = {"(": ")", "{": "}", "[": "]"}
        current_items = []

        for char in s:
            if char in paren:
                current_items.append(char)
            # not current_items to see if there is a opening bracket for current closing. 
            #pop returns the topmost character from current_items and removes it from list
            #Checks if the dictionary key does not equal closing bracket in loop (char) and then returns False
            elif not current_items or paren[current_items.pop()] != char:
                return False

        #If current_items is empty, then means all opening brackets had a closing bracket and is properly matched    
        return not current_items
