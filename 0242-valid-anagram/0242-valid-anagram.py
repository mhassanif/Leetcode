class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sx = sorted(s)
        tx = sorted(t)
        if sx==tx:
            return True
        else:
            return False
        