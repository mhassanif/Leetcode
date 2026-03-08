class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sclean = ""
        for c in s:
            if c.isalnum():
                sclean+=c.lower()
        # return s_clean==s_clean[::-1]
        start = 0
        end = len(sclean)-1
        while start<end:
            if sclean[start]==sclean[end]:
                start+=1
                end-=1
            else:
                return False
        return True