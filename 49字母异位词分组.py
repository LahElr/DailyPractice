from collections import defaultdict
from typing import List


class StringOrderUnsensitiveHash:
    def __init__(self,base,mod):
        self.base = base
        self.mod = mod
        self.count = {}

    def __reset_count(self):
        for _ in range(1,27):
            self.count[_] = 0

    def __call__(self,data):
        # 其实是可以用tuple的哈希方法的，是我傻了
        self.__reset_count()
        for c in data:
            self.count[ord(c)-96] = self.count[ord(c)-96]+1
        ret = 0
        for _ in range(1,27):
            ret+=(self.count[_]*(self.base**_))
            ret = ret%self.mod
        return ret
    
def easier_one(data):
    return hash("".join(sorted(data)))

# 9223372036854775807
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        records = defaultdict(lambda :[])
        hash_f = easier_one
        for i,s in enumerate(strs):
            records[hash_f(s)].append(i)
        ret = []
        for k in records.keys():
            ret.append([strs[i] for i in records[k]])
        return ret
    
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
strs = [""]
s = Solution()
print(s.groupAnagrams(strs))