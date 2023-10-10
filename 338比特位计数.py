r'''给你一个整数 n ，
对于 0 <= i <= n 中的每个 i ，计算其二进制表示中 1 的个数 ，
返回一个长度为 n + 1 的数组 ans 作为答案。'''

from typing import List
import math


class Solution:
    def countBits(self, n: int) -> List[int]:
        r'''
        对于i，假设j是小于等于i的最大的2的整数次幂，
        则ret[i] = ret[i-j]+1，因为实际上是在最前面加了个1
        要判别一个数是否是2的整数次幂，可用i&(i-1)==0，该式实际上将i的二进制表示中的最小的1变为0
        '''
        ret = [0,1,1,2,1,2,2,3,1]
        l = len(ret)
        j = 8
        for i in range(l,n+1):
            if i&(i-1) == 0:
                j = i
                val = 1
            else:
                val = ret[i-j]+1
            ret.append(val)
        return ret[:n+1]
    
print(Solution().countBits(16))