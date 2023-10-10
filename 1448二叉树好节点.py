r"""
给你一棵根为 root 的二叉树，请你返回二叉树中好节点的数目。
「好节点」X 定义为：从根到该节点 X 所经过的节点中，没有任何节点的值大于 X 的值。
"""

# lahelr 深度优先遍历


#!这不是个bst，不保证母子之间的关系
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(root, val):
            nonlocal res
            if not root:
                return
            if root.val >= val:
                res += 1
                val = root.val

            dfs(root.left, val)
            dfs(root.right, val)

        dfs(root, float("-inf"))
        return res


root = TreeNode(
    val=3,
    left=TreeNode(val=1, left=TreeNode(3)),
    right=TreeNode(val=4, left=TreeNode(1), right=TreeNode(5)),
)

print(Solution().goodNodes(root))
