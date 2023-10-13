class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1]<9:
            ret=digits.copy()
            ret[-1]+=1
            return ret
        elif len(digits)==1:
            return [1,0]
        else:
            ret=self.plusOne(digits[:-1])
            ret.append(0)
            return ret