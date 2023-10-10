r'''给你三个正整数 a、b 和 c。
你可以对 a 和 b 的二进制表示进行位翻转操作，
返回能够使按位或运算   a OR b == c  成立的最小翻转次数。

「位翻转操作」是指将一个数的二进制表示任何单个位上的 1 变成 0 或者 0 变成 1 。
'''

import math


class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        ans = 0
        for i in range(int(math.log2(max(a,b,c)))+1):
            base = 1<<i
            a_bit = a&base!=0
            b_bit = b&base!=0
            c_bit = c&base!=0
            # print(i,a_bit,b_bit,c_bit)
            if c_bit:
                if not (a_bit or b_bit):
                    ans +=1
            else:
                if a_bit:
                    ans+=1
                if b_bit:
                    ans+=1
        return ans


print(Solution().minFlips(8,3,5))

# 1000
# 0011
# 0101