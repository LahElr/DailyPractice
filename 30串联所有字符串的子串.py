r'''
Leetcode标的困难。困难个鬼，算法上一点也不困难，难度全在编码上
'''
from typing import List


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ret = []
        for i in range(0, len(words[0])):
            ret = ret + self.__findSubstring(s[i:], words, i)
        return ret

    def __findSubstring(self, s: str, words: List[str], starter) -> List[int]:
        if not words:
            return []
        statistics = {}
        len_words = len(words)
        len_s = len(s)
        len_word = len(words[0])
        len_serial = len_words * len_word

        for word in words:
            if word not in statistics:
                statistics[word] = 1
            else:
                statistics[word] += 1
        if len_s < len_serial:
            return []
        ret = []

        for i in range(0, len_serial, len_word):
            sub = s[i : i + len_word]
            if sub in statistics:
                statistics[sub] -= 1
        if all(statistics[_] == 0 for _ in statistics):
            ret.append(starter)
        for i in range(0, len_s - len_serial - len_word + 1, len_word):
            prev = s[i : i + len_word]
            futu = s[i + len_serial : i + len_serial + len_word]
            if prev in statistics:
                statistics[prev] += 1
            if futu in statistics:
                statistics[futu] -= 1

            if all(statistics[_] == 0 for _ in statistics):
                ret.append(i + len_word + starter)
        return ret


# s = "barfoothefoobarman"
# s = "wordgoodgoodgoodbestword"
s = "sbarfoofoobarthefoobarman"
# words = ["foo","bar"]
# words = ["word","good","best","word"]
words = ["bar", "foo", "the"]
print(Solution().findSubstring(s, words))
