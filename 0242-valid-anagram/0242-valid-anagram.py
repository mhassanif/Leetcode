class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t):
            return False
        freq= {}
        for c in s:
            freq[c] = freq.get(c,0) + 1
        for c in t:
            if c not in freq:
                return False
            freq[c]-= 1
            if freq[c] < 0:
                return False
        return True