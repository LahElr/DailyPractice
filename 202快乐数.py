def count_next(num):
    r = 0
    while num > 0:
        num, digit = divmod(num, 10)
        r += digit**2
    return r


class Solution:
    def isHappy(self, n: int) -> bool:
        slow = n
        fast = count_next(n)

        while fast != 1 and slow != fast:
            slow = count_next(slow)
            fast = count_next(count_next(fast))
        return fast == 1

    def isHappy_math(self, n: int) -> bool:
        cycle = {4, 16, 37, 58, 89, 145, 42, 20}

        while n != 1 and n not in cycle:
            n = count_next(n)
        return n == 1
