r'''
给你两个整数 left 和 right ，表示区间 [left, right] ，
返回此区间内所有数字 按位与 的结果（包含 left 、right 端点）。
'''

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        #题目限定为32位无符号整型
        r'''
        举例来说，第0位为0时，该数是偶数，只要范围内含有偶数，第0位就是0了
        将区间内所有数右移一位，范围内有偶数，第1位就是0了
        持续右移，直到left==right且是奇数，这位才是1
        后面都一样

        为什么位运算和加减是同级的啊？？？

        '''
        res = 0
        for _ in range(32):
            print(f"{1<<_}:{left}-{right}||{res}")
            if left == right:
                if left &1 :
                    res = res+(1<<_)
                    print(res)
            left = left>>1
            right = right>>1
        return res
    
    def faster_example(self,left,right):
        shift = 0
        while left<right:
            left = left>>1
            right=right>>1
            shift+=1
        return left<<shift

print(Solution().rangeBitwiseAnd(8,8))