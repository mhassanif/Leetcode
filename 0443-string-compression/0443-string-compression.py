class Solution(object):
    def compress(self, chars):
        # :type chars: List[str]
        # :rtype: int
        
        s = ""
        current = ''
        count = 0
        for char in chars:
            if char!=current:
                if count>1:
                    s+=str(count)
                current = char
                s+=current
                count = 1
            else:
                count+=1
        
        if count>1:
            s+=str(count)
        print(s)
        chars[:] = list(s)

        return len(chars)


        