r'''
给定一个 m x n 二维字符网格 board 和一个单词（字符串）列表 words， 返回所有二维网格上的单词 。

单词必须按照字母顺序，通过 相邻的单元格 内的字母构成，
其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。
同一个单元格内的字母在一个单词中不允许被重复使用。
'''

from typing import List
from collections import defaultdict
from typing import DefaultDict

def order(ch):
    return ord(ch) - 97


class TrieNode:
    def __init__(self, val=None, end_flag=False):
        self.children = DefaultDict[int,TrieNode](lambda :None)
        self.end_flag = end_flag
        self.word = ""


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
        tree_cur.word = word

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


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)

        ans = []

        m = len(board)
        n = len(board[0])
        
        def dfs(cur_node:TrieNode,i,j):
            #! the root node is empty
            if order(board[i][j]) not in cur_node.children:
                return
            ch = board[i][j]

            next_node = cur_node.children[order(ch)]

            if next_node.end_flag:
                ans.append(next_node.word)
                next_node.end_flag = False
                next_node.word = ""

            if len(next_node.children)>0:
                board[i][j] = '?'
                for ii,jj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
                    if 0<=ii<m and 0<=jj<n:
                        dfs(next_node,ii,jj)
                board[i][j] = ch #reset

            if len(next_node.children) == 0:
                cur_node.children.pop(order(ch))
        
        for i in range(m):
            for j in range(n):
                dfs(trie.root,i,j)

        return ans
    
board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
words = ["oath","pea","eat","rain"]

print(Solution().findWords(board,words))
