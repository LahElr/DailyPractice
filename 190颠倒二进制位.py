class Solution:
    def reverseBits(self, n: int) -> int:
        # 输入一个长度为32的二进制数字，输出颠倒后的数字
        # 我本以为会有个优雅的位运算或者hack加减乘除运算的方法
        # 结果没有，大失所望
        res = 0
        for _ in range(31):
            res += (n&1)
            res = res<<1
            n = n>>1
        res += (n&1)
        return res
    
print(Solution().reverseBits(43261596))