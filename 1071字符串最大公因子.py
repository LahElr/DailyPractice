r"""
对于字符串 s 和 t，
只有在 s = t + ... + t（t 自身连接 1 次或多次）时，我们才认定 “t 能除尽 s”。
给定两个字符串 str1 和 str2 。
返回 最长字符串 x，要求满足 x 能除尽 str1 且 x 能除尽 str2 。
"""

#lahelr 该子串若存，长度必定是两字符串长度的最大公约数

# str1 = "ABABAB"
# str2 = "ABAB"

str1 = "ABCABC"
str2 = "ABC"

# str1 = "ABC"
# str2 = "AB"


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        # calc gcd
        def calc_gcd(a, b):
            if a < b:
                a, b = b, a
            elif a == b:
                return a
            while True:
                c = a % b
                if c == 0:
                    return b
                else:
                    a, b = b, c

        gcd = calc_gcd(len(str1), len(str2))
        if not str1[:gcd] == str2[:gcd]:
            return ""
        solution_candidate = str1[:gcd]
        for i in range(len(solution_candidate), len(str1), len(solution_candidate)):
            if not str1[i : i + len(solution_candidate)] == solution_candidate:
                return ""
        for i in range(len(solution_candidate), len(str2), len(solution_candidate)):
            if not str2[i : i + len(solution_candidate)] == solution_candidate:
                return ""

        return solution_candidate


x = Solution()
print(x.gcdOfStrings(str1, str2))
