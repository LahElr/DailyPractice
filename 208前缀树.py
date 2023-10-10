from collections import defaultdict
from typing import DefaultDict

r'''
示例代码的优化是用字典，然后在字典中专门开一个{'end':}来放是否终结
从而将`TrieNode`省略掉变成一个{}
'''

def order(ch):
    return ord(ch) - 97


class TrieNode:
    def __init__(self, val=None, end_flag=False):
        # self.val = val
        # self.children = [None for _ in range(26)]
        self.children = DefaultDict[int,TrieNode](lambda :None)
        self.end_flag = end_flag


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        tree_cur = self.root
        for ch in word:
            child = tree_cur.children[order(ch)]
            if child:
                tree_cur = child
                continue
            child = TrieNode(ch)
            tree_cur.children[order(ch)] = child
            tree_cur = child
        tree_cur.end_flag = True

    def search(self, word: str) -> bool:
        tree_cur = self.root
        for ch in word:
            tree_cur = tree_cur.children[order(ch)]
            if tree_cur is None:
                return False
        return tree_cur.end_flag

    def startsWith(self, prefix: str) -> bool:
        tree_cur = self.root
        for ch in prefix:
            tree_cur = tree_cur.children[order(ch)]
            if tree_cur is None:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
operations = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
datas = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

obj = Trie()
op_table = {
    "Trie": lambda x: None,
    "insert": obj.insert,
    "search": obj.search,
    "startsWith": obj.startsWith,
}
for op, data in zip(operations, datas):
    if data:
        v = op_table[op](data[0])
        print(f"{v} ->", end="")
    else:
        print("None ->", end="")
