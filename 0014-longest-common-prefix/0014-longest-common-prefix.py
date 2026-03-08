class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""

        # iterate char postions
        for i in range(len(strs[0])):
            # current char check
            char = strs[0][i]
            # check evey word for this char
            for word in strs:
                if i>=len(word) or word[i]!=char:
                    # lenght exceed or mismatch
                    return prefix
            # all strings matched char - add it to prefix
            prefix+=char
        return prefix
        
        
            

