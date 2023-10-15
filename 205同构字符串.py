r'''
判断字符串同构：
如果 s 中的字符可以按某种映射关系替换得到 t ，那么这两个字符串是同构的。

每个出现的字符都应当映射到另一个字符，同时不改变字符的顺序。
不同字符不能映射到同一个字符上，相同字符只能映射到同一个字符上，字符可以映射到自己本身。
'''


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        projection_table = {}
        if len(s)!=len(t):
            return False
        for c1,c2 in zip(s,t):
            try:
                if projection_table[c1] != c2:
                    return False
                else:
                    continue
            except KeyError:
                if c2 in projection_table.values():
                    #相同字符只能映射到同一个字符上
                    return False
                projection_table[c1] = c2
                continue
        return True
    
    def __a_faster_and_cleverer_example(s,t):
        return len(set(s))==len(set(zip(s,t)))==len(set(t))


