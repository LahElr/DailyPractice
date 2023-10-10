from typing import Optional
from BinaryTree import TreeNode,build_tree,lfs_tree
class Solution:
    def pop_min(self,root):
        prev = None
        cur = root
        ret = 0
        while True:
            if cur.left is not None:
                prev = cur
                cur = cur.left
                continue
            ret = cur.val
            if prev is not None:
                prev.left = cur.right
                return root,ret
            else:
                return cur.right,ret
        
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == key:
            if root.left is None and root.right is None:
                return None
            if root.left is None and root.right is not None:
                return root.right
            if root.left is not None and root.right is None:
                return root.left
            new_right, new_val = self.pop_min(root.right)
            root.val = new_val
            root.right = new_right
            return root
        else:
            root.left = self.deleteNode(root.left,key)
            root.right = self.deleteNode(root.right,key)
            return root

root = [5,3,6,2,4,None,7]
key = 5
root = build_tree(root)
root = Solution().deleteNode(root,key)
print(lfs_tree(root))