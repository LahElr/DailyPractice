r"""一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。
机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。
问总共有多少条不同的路径？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# 用时前52.44%，内存前87.40%，直接调库comb的用时和内存居然如此之烂……？
# 代码没变又跑了一遍，用时没变，内存掉了0.3MB，提到了前36.29%…………………………
# 困惑しています.png

import math


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # C_{m+n-2}^{m-1}
        return math.comb(n + m - 2, min(m, n) - 1)


m = 3
n = 7
print(Solution().uniquePaths(m, n))
