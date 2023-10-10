r"""在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/rotting-oranges
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        stack = []
        _ = {0: -1, 1: float("inf"), 2: 0}
        i_len = len(grid)
        j_len = len(grid[0])
        time = [[_[grid[i][j]] for j in range(j_len)] for i in range(i_len)]
        for i in range(i_len):
            for j in range(j_len):
                if grid[i][j] == 2:
                    stack.append((i, j))
        positions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while stack:
            see_i, see_j = stack.pop(0)
            see_v = time[see_i][see_j]
            for position in positions:
                x = see_i + position[0]
                y = see_j + position[1]
                if x < 0 or y < 0 or x >= i_len or y >= j_len:
                    continue
                v = time[x][y]
                print(f"seeing {see_i},{see_j} of val {see_v}; at {x},{y} ,v is {v}")
                if v > see_v + 1:
                    time[x][y] = see_v + 1
                    stack.append((x, y))

        print(time)
        ret = max(max(time[i]) for i in range(i_len))
        if ret == float('inf'):
            return -1
        elif ret == -1:
            return 0
        else:
            return ret



# grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
grid = [[0]]
print(Solution().orangesRotting(grid))
