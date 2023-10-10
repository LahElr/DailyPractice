r'''
如果可以使用以下操作从一个字符串得到另一个字符串，则认为两个字符串 接近 ：

操作 1：交换任意两个 现有 字符。
例如，abcde -> aecdb
操作 2：将一个 现有 字符的每次出现转换为另一个 现有 字符，并对另一个字符执行相同的操作。
例如，aacabb -> bbcbaa（所有 a 转化为 b ，而所有的 b 转换为 a ）
你可以根据需要对任意一个字符串多次使用这两种操作。

给你两个字符串，word1 和 word2 。如果 word1 和 word2 接近 ，就返回 true ；否则，返回 false 。
'''

#lahelr 字符集相同且字符出现次数（不保序）相等

word1 = "abc"
word2 = "bca"

class Solution(object):
    def __init__(self):
        pass

    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        if not len(word1) == len(word2):
            return False
        
        set_w1 = set(list(word1))
        set_w2 = set(list(word2))
        if not len(set_w1.intersection(set_w2)) == len(set_w1) == len(set_w2):
            return False
        del set_w2,set_w1

        def count_word(word):
            ret = [0 for _ in range(26)]
            for char in word:
                ret[ord(char)-97] += 1
            return ret
        
        count1 = count_word(word1)
        count2 = count_word(word2)

        return sorted(count1) == sorted(count2)

        

sol = Solution()
print(sol.closeStrings(word1,word2))