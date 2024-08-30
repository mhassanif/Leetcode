class Solution(object):
    def gcdOfStrings(self, str1, str2):

        # for gcd of string lengths
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        
        # checks if a string t divides s
        def divides(s, t):
            return t * (len(s) // len(t)) == s
        
        # gcd of lengths
        gcd_len = gcd(len(str1), len(str2))
        
        # substring of gcd length
        candidate = str1[:gcd_len]
        
        # Check if it divides both
        if divides(str1, candidate) and divides(str2, candidate):
            return candidate
        else:
            return ""
