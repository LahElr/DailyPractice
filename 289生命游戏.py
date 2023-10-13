from typing import List

r"""
如果活细胞周围八个位置的活细胞数少于两个，则该位置活细胞死亡；
如果活细胞周围八个位置有两个或三个活细胞，则该位置活细胞仍然存活；
如果活细胞周围八个位置有超过三个活细胞，则该位置活细胞死亡；
如果死细胞周围正好有三个活细胞，则该位置死细胞复活；
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        返回下一个状态
        """

        # define of status:
        # 0:dead, and will be dead
        # 1:live, but will be dead
        # 2:dead, but will be live
        # 3:live, and will be live
        def __get_current_status(n):
            return n % 2

        def __get_future_status(n):
            return n // 2

        def countView(x, y):
            # assert x>=0 and y>=0
            ret = 0
            for line in board[max(x - 1, 0) : x + 2]:
                ret += sum(map(__get_current_status, line[max(y - 1, 0) : y + 2]))
            return ret

        m = len(board)
        n = len(board[0])
        for x in range(m):
            for y in range(n):
                v = countView(x, y)
                print(f"{x},{y}->[{board[x][y]}]->{v}")
                if __get_current_status(board[x][y]):
                    # remember here the view counting includes this cell itself
                    if v <= 2:
                        board[x][y] = 1
                    elif v <= 4:
                        board[x][y] = 3
                    else:
                        board[x][y] = 1
                else:
                    if v == 3:
                        board[x][y] = 2
        print(board)
        for x in range(m):
            for y in range(n):
                board[x][y] = __get_future_status(board[x][y])

b = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Solution().gameOfLife(b)
print(b)