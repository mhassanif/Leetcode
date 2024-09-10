# :type s: str
# :type k: int
# :rtype: int

class Solution(object):
    def maxVowels(self, s, k):
        vowels = ['a', 'e', 'i', 'o', 'u']
        maxVowels = 0
        vowelCount = 0
        for i in range(k):
            if s[i] in vowels:
                vowelCount+=1
        maxVowels = vowelCount
        start = 0
        end = k
        while end<len(s):
            # print(s[start:end])
            if s[start] in vowels:
                vowelCount-=1
            if s[end] in vowels:
                vowelCount+=1
            if vowelCount>maxVowels:
                maxVowels = vowelCount
            start+=1
            end+=1
        return maxVowels
            


        