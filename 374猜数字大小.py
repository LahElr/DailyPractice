r'''
猜数字游戏的规则如下：

每轮游戏，我都会从 1 到 n 随机选择一个数字。 请你猜选出的是哪个数字。
如果你猜错了，我会告诉你，你猜测的数字比我选出的数字是大了还是小了。
你可以通过调用一个预先定义好的接口 int guess(int num) 来获取猜测结果，返回值一共有 3 种可能的情况（-1，1 或 0）：

-1：我选出的数字比你猜的数字小 pick < num
1：我选出的数字比你猜的数字大 pick > num
0：我选出的数字和你猜的数字一样。恭喜！你猜对了！pick == num
返回我选出的数字。
'''

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

n=2
pick=1

class Guess():
    def __init__(self,pick):
        self.pick = pick
    def __call__(self,num):
        if self.pick<num:
            return -1
        elif self.pick > num:
            return 1
        else:
            return 0
        
guess = Guess(pick)

class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        while True:
            this_guess = left + (right-left)//2
            result = guess(this_guess)
            if result == -1:
                right = this_guess
            elif result == 1:
                left = this_guess+1
            else:
                return this_guess

print(Solution().guessNumber(n))