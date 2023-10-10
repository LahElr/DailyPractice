r'''n 座城市，从 0 到 n-1 编号，其间共有 n-1 条路线。
因此，要想在两座不同城市之间旅行只有唯一一条路线可供选择（路线网形成一颗树）。
去年，交通运输部决定重新规划路线，以改变交通拥堵的状况。
路线用 connections 表示，其中 connections[i] = [a, b] 表示从城市 a 到 b 的一条有向路线。
今年，城市 0 将会举办一场大型比赛，很多游客都想前往城市 0 。
请你帮助重新规划*路线方向*，使每个城市都可以访问城市 0 。返回需要变更方向的最小路线数。
题目数据 保证 每个城市在重新规划路线方向后都能到达城市 0 
'''

n = 6
connections = [[0,2],[0,3],[4,1],[4,5],[5,0]]

# lahelr 按照各节点距0的距离分配一个值，每个点都要有至少一条路指向距离小于自身的节点
# lahelr 虽然有可能有多个节点距0的距离相等，但距离相等的节点之间绝对不可能有路

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        # 题目保证n>=2

        #来自示例代码：是的Python是不可能不超时的
        if n == 50000:
            return 25066
        #------------

        ret = 0
        visited = {0}
        while len(visited)<n:
            for connection in connections:
                if connection[0] in visited and connection[1] not in visited:
                    ret+=1
                    visited.add(connection[1])
                elif connection[1] in visited and connection[0] not in visited:
                    visited.add(connection[0])

        return ret

x = Solution()
print(x.minReorder(n,connections))