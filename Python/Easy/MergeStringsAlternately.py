class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        new_string = ""
        length_word1_items = []
        length_word2_items = []
        length_word1, length_word2 = len(word1), len(word2)

        for i in word1:
            length_word1_items.append(i)
        for i in word2:
            length_word2_items.append(i)
        
        if len(word1) > len(word2):
            max_word = len(word1)
        else:
            max_word = len(word2)

        for i in range (max_word):
            if i < len(word1):
                new_string = new_string + length_word1_items[i]
            if i < len(word2):
                new_string = new_string + length_word2_items[i]
            
        return new_string
