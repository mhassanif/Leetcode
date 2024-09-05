class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "":
            return True
        s_index = 0
        for c in t:
            if c == s[s_index]:
                print(s[s_index])
                s_index+=1
                if s_index>=len(s):
                    #all have been found
                    return True
        return False
        