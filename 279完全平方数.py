r'''求取将一个数表示为完全平方数的和所需的最少数量'''
import math

class Solution:
    def __numSquares(self, n: int) -> int:
        r'''动态规划'''
        if n == 1:
            return 1
        solutions = [0 for _ in range(n+1)]
        for i in range(1,n+1):
            cand = float('inf')
            for j in range(1,i+1):
                if j**2 > i:
                    break
                cand = min(cand,solutions[i-j**2])
            solutions[i] = cand+1
        return solutions[-1]
    def numSquares(self, n: int) -> int:
        r'''四平方和定理'''
        def is_square(x):
            y = math.isqrt(x)
            return y**2 == x
        if is_square(n):
            return 1
        
        _n = n
        while _n%4 == 0:
            _n = _n//4
        if _n % 8 == 7:
            return 4
        
        for i in range(1,math.isqrt(n)+1):
            if is_square(n-i**2):
                return 2
            
        return 3
