r'''有两种形状的瓷砖：一种是 2 x 1 的多米诺形，另一种是形如 "L" 的托米诺形。两种形状都可以旋转。
给定整数 n ，返回可以平铺 2 x n 的面板的方法的数量。返回对 10**9 + 7 取模 的值。

平铺指的是每个正方形都必须有瓷砖覆盖。
两个平铺不同，当且仅当面板上有四个方向上的相邻单元中的两个，使得恰好有一个平铺有一个瓷砖占据两个正方形。'''

class Solution:
    def numTilings(self, n: int) -> int:
        r'''
        考虑这么一种平铺的方式：在第 i 列前面的正方形都被瓷砖覆盖，在第 i 列后面的正方形都没有被瓷砖覆盖
        （i 从 1开始计数）。
        那么第 iii 列的正方形有四种被覆盖的情况：
        一个正方形都没有被覆盖，记为状态 0
        只有上方的正方形被覆盖，记为状态 1
        只有下方的正方形被覆盖，记为状态 2
        上下两个正方形都被覆盖，记为状态 3
        题目保证n>=1
        '''
        prev_row = [0,0,0,1]
        this_row = [1,1,1,2]
        n-=2
        if n == -1:
            return prev_row[3]
        if n == 0:
            return this_row[3]
        for i in range(n):
            prev_row,this_row = this_row,prev_row
            # this_row = [0,0,0,0]
            this_row[0] = prev_row[3]
            this_row[1] = prev_row[0]+prev_row[2]
            this_row[2] = prev_row[0]+prev_row[1]
            this_row[3] = prev_row[0]+prev_row[1]+prev_row[2]+prev_row[3]
        return this_row[3]
    
print(Solution().numTilings(4))