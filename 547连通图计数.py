r"""
有 n 个城市，其中一些彼此相连，另一些没有相连。
如果城市 a 与城市 b 直接相连，且城市 b 与城市 c 直接相连，那么城市 a 与城市 c 间接相连。
省份 是一组直接或间接相连的城市，组内不含其他没有相连的城市。
给你一个 n x n 的矩阵 isConnected ，
其中 isConnected[i][j] = 1 表示第 i 个城市和第 j 个城市直接相连，
而 isConnected[i][j] = 0 表示二者不直接相连。
返回矩阵中 省份 的数量。
"""
r'''
连通图计数，通过将 此前未见的节点 作为根节点进行图遍历 来进行图区分
执行用时占前0.91%，内存占前2.74%，我一定要炫耀一下
O(N^2),O(2N)
'''
# isConnected = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
isConnected = [[1,0,0,1],
               [0,1,1,0],
               [0,1,1,1],
               [1,0,1,1]]


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """
        n = len(isConnected)
        if n == 1:
            return 1
        graph_count = 0
        nodes_visited = [False for _ in range(n)]
        for i in range(n):
            if nodes_visited[i]:
                continue

            print(f"new node {i}")
            this_graph_stack = [i]
            graph_count += 1
            nodes_visited[i] = True

            while len(this_graph_stack) > 0:
                print(f"stack:{this_graph_stack}")
                this_node = this_graph_stack.pop(0)
                for candidate_node in range(n):
                    # 如果超限，自动为空
                    if (
                        not nodes_visited[candidate_node]
                        and isConnected[this_node][candidate_node] == 1
                    ):
                        nodes_visited[candidate_node] = True
                        this_graph_stack.append(candidate_node)
        return graph_count


x = Solution()
print(x.findCircleNum(isConnected))
