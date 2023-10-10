r"""
给你一个变量对数组 equations 和一个实数值数组 values 作为已知条件，
其中 equations[i] = [Ai, Bi] 和 values[i] 共同表示等式 Ai / Bi = values[i] 。
每个 Ai 或 Bi 是一个表示单个变量的*字符串*。

另有一些以数组 queries 表示的问题，
其中 queries[j] = [Cj, Dj] 表示第 j 个问题，
请你根据已知条件找出 Cj / Dj = ? 的结果作为答案。

返回 所有问题的答案 。
如果存在某个无法确定的答案，则用 -1.0 替代这个答案。
如果问题中出现了给定的已知条件中没有出现的字符串，也需要用 -1.0 替代这个答案。

注意：输入总是有效的。你可以假设除法运算中不会出现除数为 0 的情况，且不存在任何矛盾的结果。
"""

from collections import deque
from typing import List


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        r"""
        有向图？
        s/t = s/p * p/t\
          a   b   c   bc   cd
        a 1   1/2 *1/6
        b 2   1   1/3
        c *6  3   1
        bc             1   1/5
        cd             5   1
        我是不是还得考虑小数精度啊？
        他干嘛给我字符串不直接给我表格索引啊？
        这个表格是要用什么顺序遍历啊
        从给定的第一个开始ab，检查b列，补齐所有ab?序列，然后把这些新加的a?点压进队列
        为了保证不漏，初始队列还得加上所有反向
        好家伙，我这个算法这么复杂居然还能在时间上击败72.19%的用户？！
        """
        # lahelr 统计表头
        str_ct = 0
        str_to_index_dict = {}
        for eq1, eq2 in equations:
            if eq1 not in str_to_index_dict:
                str_to_index_dict[eq1] = str_ct
                str_ct += 1
            if eq2 not in str_to_index_dict:
                str_to_index_dict[eq2] = str_ct
                str_ct += 1
        for eq in equations:
            eq[0] = str_to_index_dict[eq[0]]
            eq[1] = str_to_index_dict[eq[1]]
        # lahelr建表
        matrix_size = len(str_to_index_dict)
        matrix = [[-1.0 for j in range(matrix_size)] for i in range(matrix_size)]
        # lahelr填入初始数值
        for i in range(matrix_size):
            matrix[i][i] = 1.0
        for (i, j), v in zip(equations, values):
            matrix[i][j] = v
            matrix[j][i] = 1 / v
        # lahelr 开始遍历
        equations.extend([[eq2,eq1] for eq1,eq2 in equations])
        queue = deque(equations)
        while queue:
            a, b = queue.popleft()
            base_val = matrix[a][b]
            for c, v in enumerate(matrix[b]):
                if v == -1.0:
                    continue
                val = base_val * v  # [a,b]*[b,c]
                tgt_val = matrix[a][c]
                if tgt_val == -1.0:
                    matrix[a][c] = val
                    matrix[c][a] = 1 / val
                    queue.append([a, c])
        print(matrix)
        print(str_to_index_dict)
        ans = []
        for q1, q2 in queries:
            try:
                a = str_to_index_dict[q1]
                b = str_to_index_dict[q2]
            except KeyError:
                ans.append(-1.0)
                continue
            val = matrix[a][b]
            if val < 0:
                ans.append(-1.0)
                continue
            ans.append(val)
        return ans


equations = [["x1","x2"],["x2","x3"],["x1","x4"],["x2","x5"]]
values = [3.0,0.5,3.4,5.6]
queries = [["x2","x4"],["x1","x5"],["x1","x3"],["x5","x5"],["x5","x1"],["x3","x4"],["x4","x3"],["x6","x6"],["x0","x0"]]

print(Solution().calcEquation(equations, values, queries))
