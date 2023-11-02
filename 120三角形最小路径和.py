r"""
给定一个三角形 triangle ，找出自顶向下的最小路径和。

每一步只能移动到下一行中相邻的结点上。
相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点。
也就是说，如果正位于当前行的下标 i ，那么下一步可以移动到下一行的下标 i 或 i + 1 。
"""

from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i, line in enumerate(triangle[1:]):
            # i = i+1
            for j, x in enumerate(line):
                if j > 0:
                    a = triangle[i][j - 1]
                else:
                    a = 100000
                try:
                    b = triangle[i][j]
                except IndexError:
                    b = 100000
                # print(i, j, a, b)
                triangle[i + 1][j] = x + min(a, b)
            # print(triangle[i + 1])
        return min(triangle[-1])


# triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
triangle = [[-1], [3, 2], [-3, 1, -1]]

print(Solution().minimumTotal(triangle))
