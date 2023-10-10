word1 = "sea"
word2 = "eat"


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        x = len(word1)
        y = len(word2)

        if x == 0 or y == 0:
            return max(x, y)

        # numpy.zeros(x,y)
        sol_matrix = [[-1] * (y + 1) for _ in range(x + 1)]

        sol_matrix[0][0] = 0
        for i in range(0, x + 1):
            sol_matrix[i][0] = i
        for j in range(0, y + 1):
            sol_matrix[0][j] = j

        for i in range(1, x + 1):
            for j in range(1, y + 1):
                sol_matrix[i][j] = min(
                    sol_matrix[i - 1][j - 1]
                    + (0 if word1[i - 1] == word2[j - 1] else 1),
                    sol_matrix[i - 1][j] + 1,
                    sol_matrix[i][j - 1] + 1,
                )

        print(sol_matrix)
        return sol_matrix[-1][-1]

    def minDistanceExample(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        # 超级优化过的示例代码
        # 主要是跳过了相同子串，也就是斜线代价为0时就使劲用
        # 还有将表格作为图进行广度优先搜索
        queue = [(word1, word2, 0)]
        visited = set()
        while queue:
            word1, word2, value = queue.pop(0)
            while word1 and word2 and word1[0] == word2[0]:
                word1 = word1[1:]
                word2 = word2[1:]
            if (word1, word2) in visited:
                continue
            if word1 == word2:
                return value
            visited.add((word1, word2))
            queue += [
                (word1, word2[1:], value + 1),
                (word1[1:], word2, value + 1),
                (word1[1:], word2[1:], value + 1),
            ]


x = Solution()
print(x.minDistance(word1, word2))
