r'''
给定一个二叉树的根节点 root，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。
路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
'''
import collections
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

tree = TreeNode(8,
    left=TreeNode(5,
        left=TreeNode(3,
            left=TreeNode(3),
            right=TreeNode(-2)),
        right=TreeNode(2,
            right=TreeNode(1))),
    right=TreeNode(-3,
        right=TreeNode(11)))

targetSum=8

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """

        self.lahelr_ret = 0

        def lfs_tree(root,parent_note=None):
            if root is None:
                return
            if parent_note is None:
                lfs_tree(root.left,[root.val])
                lfs_tree(root.right,[root.val])
                if root.val == targetSum:
                    self.lahelr_ret+=1
                return
            note = [_ + root.val for _ in parent_note]
            note.append(root.val)
            for i in range(len(note)):
                if note[i]==targetSum:
                    self.lahelr_ret+=1
            lfs_tree(root.left,note)
            lfs_tree(root.right,note)

            print(root.val,note)

        lfs_tree(root)
        return self.lahelr_ret

x = Solution()
print(x.pathSum(tree,targetSum))

