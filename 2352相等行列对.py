r'''给你一个下标从 0 开始、大小为 n x n 的整数矩阵 grid ，
返回满足 Ri 行和 Cj 列相等的行列对 (Ri, Cj) 的数目。
如果行和列以相同的顺序包含相同的元素（即相等的数组），则认为二者是相等的。
'''

from collections import Counter
from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 1
        counter = Counter(tuple(row) for row in grid)
        ret = 0
        for j in range(n):
            ret+=counter[tuple(grid[i][j] for i in range(n))]
        return ret

grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
print(Solution().equalPairs(grid))