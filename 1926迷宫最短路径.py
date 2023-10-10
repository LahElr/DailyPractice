r"""给你一个 m x n 的迷宫矩阵 maze （下标从 0 开始）, 
矩阵中有空格子（用 '.' 表示）和墙（用 '+' 表示）。
同时给你迷宫的入口 entrance , 
用 entrance = [entrancerow, entrancecol] 表示你一开始所在格子的行和列。
每一步操作, 你可以往 上, 下, 左 或者 右 移动一个格子。
你不能进入墙所在的格子, 你也不能离开迷宫。
你的目标是找到离 entrance 最近 的出口。
出口 的含义是 maze 边界 上的 空格子。entrance 格子 不算 出口。
请你返回从 entrance 到最近出口的最短路径的 步数,
如果不存在这样的路径, 请你返回 -1 。
"""

maze = [
    [".", ".", ".", ".", ".", "+", ".", ".", "."],
    [".", "+", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", "+", ".", "+", ".", "+", ".", "+"],
    [".", ".", ".", ".", "+", ".", ".", ".", "."],
    [".", ".", ".", ".", "+", "+", ".", ".", "."],
    ["+", ".", ".", ".", ".", ".", ".", ".", "."],
    [".", ".", ".", "+", ".", ".", ".", ".", "."],
    [".", ".", ".", "+", ".", ".", ".", ".", "+"],
    ["+", ".", ".", "+", ".", "+", "+", ".", "."],
]
entrance = [8, 4]


class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        nodes_need_to_see = [entrance]
        maze[entrance[0]][entrance[1]] = 0

        max_x = len(maze)
        max_y = len(maze[0])

        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def vec_add(a, b):
            return [i + j for i, j in zip(a, b)]

        while True:
            if len(nodes_need_to_see) == 0:
                break
            node_to_see = nodes_need_to_see.pop()
            # print("see",node_to_see)
            for direction in directions:
                node_x = node_to_see[0] + direction[0]
                node_y = node_to_see[1] + direction[1]

                if node_x < 0 or node_x >= max_x or node_y < 0 or node_y >= max_y:
                    continue
                if maze[node_x][node_y] == "+":
                    continue
                elif maze[node_x][node_y] == ".":
                    node_answer = maze[node_to_see[0]][node_to_see[1]] + 1
                    nodes_need_to_see.insert(0,[node_x, node_y])
                    # print("add",node_x,node_y, node_answer)
                else:
                    if maze[node_to_see[0]][node_to_see[1]] + 1 < maze[node_x][node_y]:
                        node_answer = maze[node_to_see[0]][node_to_see[1]] +1
                        nodes_need_to_see.insert(0,[node_x, node_y])
                        # print("add",node_x,node_y, node_answer)
                    else:
                        continue

                maze[node_x][node_y] = node_answer

                if (
                    (
                        node_x == 0
                        or node_x == max_x - 1
                        or node_y == 0
                        or node_y == max_y - 1
                    )
                    and node_answer != 0
                ):
                    return node_answer
        # print(maze)
        return -1


x = Solution()
print(x.nearestExit(maze, entrance))
