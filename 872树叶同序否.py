r"""
请考虑一棵二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个 叶值序列 。
如果有两棵二叉树的叶值序列是相同，那么我们就认为它们是 叶相似 的。
"""
#lahelr 深度优先遍历

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


tree1 = TreeNode(
    3,
    left=TreeNode(5, 
        left=TreeNode(6), 
        right=TreeNode(
            2, 
            left=TreeNode(7),
            right=TreeNode(4))),
    right=TreeNode(1, 
        left=TreeNode(9), 
        right=TreeNode(8))
)

tree2 = TreeNode(3,
    left=TreeNode(5, 
        left=TreeNode(6), 
        right=TreeNode(7)),
    right = TreeNode(1,
        left=TreeNode(4),
        right=TreeNode(2,
            left=TreeNode(9),
            right=TreeNode(8)))
)


class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
    
        def lfs_leaves(tree):
            if tree is None:
                return []
            if tree.left is None and tree.right is None:
                return [tree.val]
            else:
                return lfs_leaves(tree.left)+lfs_leaves(tree.right)
        
        return lfs_leaves(root1) == lfs_leaves(root2)

x = Solution()
print(x.leafSimilar(tree1, tree2))
