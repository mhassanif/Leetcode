class Solution(object):
    def reverseWords(self, s):
        result = ""
        # splits string into a list.
        words = s.split()
        # joins words in reverse into one string with ' ' as the separator.
        return ' '.join(reversed(words))


#iterate words in reverse and concat to result
# for word in reversed(words):
#    result += word + ' '
# # remove trailing spaces and return
# return result.strip()
        