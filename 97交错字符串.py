class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        a = len(s1)
        b = len(s2)
        c = len(s3)
        if a + b != c:
            return False
        if a == 0:
            return s2 == s3
        if b == 0:
            return s1 == s3

        matrix = [[False for j in range(b + 1)] for i in range(a + 1)]
        matrix[0][0] = True

        for i in range(1, a + 1):
            if s1[i - 1] == s3[i - 1]:
                matrix[i][0] = True
            else:
                break

        for j in range(1, b + 1):
            if s2[j - 1] == s3[j - 1]:
                matrix[0][j] = True
            else:
                break

        for i in range(1, a + 1):
            for j in range(1, b + 1):
                if (matrix[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (
                    matrix[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                ):
                    matrix[i][j] = True

        print(matrix)
        return matrix[-1][-1]

    def isInterleave_optimized(self, s1: str, s2: str, s3: str) -> bool:
        # 这个算法在leetcode上的内存占用一点没比上面那个少，对leetcode的统计深表怀疑
        a = len(s1)
        b = len(s2)
        c = len(s3)
        if a + b != c:
            return False
        if a == 0:
            return s2 == s3
        if b == 0:
            return s1 == s3

        # matrix = [[False for j in range(b + 1)] for i in range(a + 1)]
        prev = [False for j in range(b + 1)]
        prev[0] = True
        for j in range(1, b + 1):
            if s2[j - 1] == s3[j - 1]:
                prev[j] = True
            else:
                break
        print(prev)
        this_0_flag = True

        for i in range(1, a + 1):
            this = [False for j in range(b + 1)]
            if s1[i - 1] == s3[i - 1]:
                if this_0_flag:
                    this[0] = True
            else:
                this_0_flag = False

            for j in range(1, b + 1):
                if (prev[j] and s1[i - 1] == s3[i + j - 1]) or (
                    this[j - 1] and s2[j - 1] == s3[i + j - 1]
                ):
                    this[j] = True

            print(this)
            prev = this

        return this[-1]


# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"

# s1 = "aa"
# s2 = "ab"
# s3 = "aaba"

s1 = "db"
s2 = "b"
s3 = "cbb"

print(Solution().isInterleave(s1, s2, s3))
print(Solution().isInterleave_optimized(s1, s2, s3))
