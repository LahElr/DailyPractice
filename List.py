import bisect
from collections import defaultdict
from typing import List


def longestCommonSubsequence(s1: str, s2: str) -> int:
    r"""
    搜索 “最长 公共 不连续 子串” 的长度
    """

    def LCS(_s1: str, _s2: str) -> int:
        # 请保证: len(s1) <= len(s2)
        m = len(_s2)
        mapper = defaultdict[str, List[int]](list)
        for i in reversed(range(m)):
            mapper[_s2[i]].append(i)  # 记录各个字母各次出现时的索引
        nums = []
        for c in _s1:
            if c in mapper:
                nums.extend(mapper[c])  # [各个1字母在2中出现的顺序]
        return LIS(nums)

    def LIS(nums: List[int]) -> int:
        """O(nlogn)"""
        stack = []
        for x in nums:
            idx = bisect.bisect_left(stack, x)
            if idx < len(stack):
                stack[idx] = x  # 它会顶掉那个刚好比它大的数
            else:
                stack.append(x)
        # 此时stack里记录的就是最大公共子序列各字在长字符串中的索引
        # （解的一种）
        return len(stack)

    n, m = len(s1), len(s2)
    if n > m:
        return longestCommonSubsequence(s2, s1)
    # n <= m
    if s1 in s2:
        return n
    return LCS(s1, s2)


def isSubsequence(s: str, t: str) -> bool:
    r"""判断s是否是t的不连续子序列"""
    scur = 0
    tcur = 0
    slen = len(s)
    tlen = len(t)
    if tlen < slen:
        return False
    while True:
        if scur >= slen:
            return True
        if tcur >= tlen:
            return False
        sval = s[scur]
        tval = t[tcur]
        if sval == tval:
            scur += 1
        tcur += 1
    return None


def edit_distance(self, word1, word2):
    r"""
    编辑距离
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


class KMP_string_match:
    r"""Knuth-Morris-Pratt string matching algorithm"""

    def __init__(self):
        pass

    @classmethod
    def pi(cls, s):
        r"""The prefix function `pi`
        for a string `s` of length `m`, pi(i) (0<=i<m) means:
            the largest length of the equal real-prefix and real-suffix of `s[0:i+1]`
            or 0 if such prefix and suffix do not exist
        pi(i) <= pi(i-1)+1
        pi(i) == pi(i-1)+1 if s[i] == s[pi(i-1)]

        find the max j, s.t. s[0:j] == s[i-j:i] and s[i] == s[j]
            therefor s[0:j+1] == s[i-j:i+1], i.e. pi(i) == j+1
        since s[0:pi(i-1)] == s[i-pi(i-1):i]
        then if s[i] == s[pi(i-1)], pi(i) = j+1
        if not, then pi(i) <= pi(i-1) <==> j < pi(i-1)
            therefor, s[pi(i-1)-j:pi(i-1)] == s[i-j:i]
            then we could find the max j, s.t.
                s[0:j] == s[pi(i-1)-j:pi(i-1)] and s[i] == s[j]
            then if s[i] == s[pi(pi(i-1)-1)], we know:
                j = pi(pi(i-1)-1), and
                pi(i) = j+1
            if not, then pi(i) <= pi(pi(i-1)-1) <==> j < pi(pi(i-1)-1)
                ...

        hence we could find that j always follow a structure of:
            pi(pi(pi(...)-1)-1)
        therefore we could recurse from j=pi(i-1) -> j=pi(j-1) -> ...
            until s[i] == s[j] or j == 0
            once match successes (s[i] == s[j]), we would know pi(i)=j+1
        or pi(i) = 0
        """
        m = len(s)
        ret = [0 for _ in range(m)]
        for i in range(1, m):
            j = ret[i - 1]
            while True:
                if s[i] == s[j]:
                    ret[i] = j + 1
                    break
                if j <= 0:
                    ret[i] = 0
                    break
                j = ret[j - 1]
        return ret

    @classmethod
    def string_match(cls, pattern, target):
        m = len(pattern)
        # n = len(target)

        merged = pattern + "#" + target
        pi = cls.pi(merged)
        for i, _ in enumerate(pi[m + 1 :]):
            if _ == m:
                return i


def gray_code(n):
    assert isinstance(n, int) and n >= 1
    return [(i >> 1) ^ i for i in range(1 << n)]
