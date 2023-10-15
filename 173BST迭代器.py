# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
r"""
中序遍历，也就是树元素排序……
调用next时，从最左侧点开始
每次调用时，若有右子节点，则移动到右子节点的最左子点
若无，则沿路径向前移动
"""

r'''
最快和最省内存的解法是直接中序遍历完存起来，草（中日双语
甚至直接用的递归
'''
from typing import Optional
from BinaryTree import TreeNode, build_tree


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        cur = root
        self.stack = []

        self.search_left(cur)

    def search_left(self, cur):
        while True:
            if cur.left is not None:
                self.stack.append(cur)
                cur = cur.left
            else:
                self.stack.append(cur)
                break

    def next(self) -> int:
        try:
            ret = self.stack.pop()
        except IndexError:
            raise StopIteration()
        if ret.right is not None:
            cur = ret.right
            self.search_left(cur)
        return ret.val

    def hasNext(self) -> bool:
        return len(self.stack) > 0


root = build_tree([7, 3, 15, None, None, 9, 20])
obj = BSTIterator(root)
