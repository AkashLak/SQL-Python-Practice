class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = "aeiouAEIOU"
        #Convert string to a list for more flexability
        s = list(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] not in vowels:
                i = i + 1
                #Entire iteraton of loop is skipped if continue is reached
                continue
            if s[j] not in vowels:
                j = j - 1
                continue
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            #Need to implement i and j counter twice for fail and pass
            i = i + 1
            j = j - 1
        #New string needs to be outside of while loop, otherwise would be reset everytime
        new_string = ""
        #Cant have same loop variable as i or j, so using char
        for char in s:
            new_string = new_string + char
        return new_string
