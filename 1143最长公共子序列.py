r"""给定两个字符串 text1 和 text2，
返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的 子序列 是指这样一个新的字符串：
它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-common-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


from bisect import bisect_left
from collections import defaultdict
from typing import DefaultDict, List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dynamic_matrix = [
            [0 for _ in range(len(text2) + 1)] for __ in range(len(text1) + 1)
        ]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dynamic_matrix[i + 1][j + 1] = dynamic_matrix[i][j] + 1
                else:
                    dynamic_matrix[i + 1][j + 1] = max(
                        dynamic_matrix[i][j + 1], dynamic_matrix[i + 1][j]
                    )
        # print(dynamic_matrix)
        return dynamic_matrix[-1][-1]


text1 = "bmvcnwrmxcfcxabkxcvgbozmpspsbenazglyxkpibgzq"
text2 = "bmpmlstotylonkvmhqjyxmnqzctonqtobahcrcbibgzgx"
print(Solution().longestCommonSubsequence(text1, text2))


class Solution:
    """recommended"""

    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)
        if n > m:
            return self.longestCommonSubsequence(s2, s1)
        # n <= m
        if s1 in s2:
            return n
        return LCS(s1, s2)


def LCS(s1: str, s2: str) -> int:
    # 请保证: len(s1) <= len(s2)
    m = len(s2)
    mapper = DefaultDict[str, List[int]](list)
    for i in reversed(range(m)):
        mapper[s2[i]].append(i)  # 记录各个字母各次出现时的索引
    nums = []
    for c in s1:
        if c in mapper:
            nums.extend(mapper[c])  # [各个1字母在2中出现的顺序]
    return LIS(nums)


def LIS(nums: List[int]) -> int:
    """O(nlogn)"""
    stack = []
    for x in nums:
        idx = bisect_left(stack, x)
        if idx < len(stack):
            stack[idx] = x  # 它会顶掉那个刚好比它大的数
        else:
            stack.append(x)
    # 此时stack里记录的就是最大公共子序列各字在长字符串中的索引
    # （解的一种）
    return len(stack)
