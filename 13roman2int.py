class Solution:
    def romanToInt(self, s: str) -> int:
        mapper = {'I':1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        if len(s)==1:
            return mapper[s]
        ret = 0
        i=0
        l = len(s)
        while True:
            if i >= l:
                break
            if i == l-1:
                ret+=mapper[s[i]]
                break
            this_digit = mapper[s[i]]
            next_digit = mapper[s[i+1]]

            if this_digit<next_digit:
                ret+=(next_digit-this_digit)
                i+=2
            else:
                ret+=this_digit
                i+=1
        return ret

print(Solution().romanToInt('MCMXCIV'))
