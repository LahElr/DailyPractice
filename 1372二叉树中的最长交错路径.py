r"""给你一棵以 root 为根的二叉树，二叉树中的交错路径定义如下：

选择二叉树中 任意 节点和一个方向（左或者右）。
如果前进方向为右，那么移动到当前节点的的右子节点，否则移动到它的左子节点。
改变前进方向：左变右或者右变左。
重复第二步和第三步，直到你在树中无法继续移动。
交错路径的长度定义为：访问过的节点数目 - 1（单个节点的路径长度为 0 ）。

请你返回给定树中最长 交错路径 的长度。"""

from collections import defaultdict
from typing import Optional
from BinaryTree import TreeNode, build_tree, lfs_tree


class Solution:
    def longestZigZag_dp(self, root: Optional[TreeNode]) -> int:
        r"""
        left[n]为自根至n且n是其母左子的最长交错路径
        right[n] vice versa
        left[n] = right[n.parent]+1
        right[n] = left[n.parent]+1
        然后遍历树
        """
        right = defaultdict(lambda:0)
        left = defaultdict(lambda:0)
        dfs_stack = [(root, None)]
        while dfs_stack:
            cur, parent = dfs_stack.pop()
            if parent:
                if parent.left == cur:
                    left[cur] = right[parent] + 1
                else:
                    right[cur] = left[parent] + 1
            if cur.left:
                dfs_stack.append((cur.left, cur))
            if cur.right:
                dfs_stack.append((cur.right, cur))
        return max(max(right.values()), max(left.values()))
    
    def longestZigZag(self,root:Optional[TreeNode]=None)->int:
        # optimum, profundum primum quaerere
        if not root:
            return 0
        dfs_stack = []
        ret = 0
        if root.left:
            dfs_stack.append((root.left,0,1))
        if root.right:
            dfs_stack.append((root.right,1,1))
        while dfs_stack:
            cur,direction,val = dfs_stack.pop()
            # derection: 0是左子，1是右子
            ret = max(ret,val)
            if direction == 0:
                if cur.right:
                    dfs_stack.append((cur.right,1,val+1))
                if cur.left:
                    dfs_stack.append((cur.left,0,1))
            else:
                if cur.left:
                    dfs_stack.append((cur.left,0,val+1))
                if cur.right:
                    dfs_stack.append((cur.right,1,1))
        return ret


root = [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1]
tree = build_tree(root)
print(Solution().longestZigZag(tree))
