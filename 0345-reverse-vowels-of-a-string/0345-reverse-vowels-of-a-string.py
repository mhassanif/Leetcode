#  # :type s: str
# # :rtype: str

class Solution(object):
    def reverseVowels(self, s):
        string = list(s)
        vowels = set('aeiouAEIOU')  # set --> faster lookup
        i = 0
        j = len(s)-1
        while i<j:
            if string[i] not in vowels:
                i+=1
            if string[j] not in vowels:
                j-=1

            if string[i] in vowels and string[j] in vowels:
                string[i], string[j] = string[j], string[i]  #swap
                i+=1
                j-=1

        return ''.join(string)
