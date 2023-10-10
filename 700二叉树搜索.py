
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root is None:
            return None
        cur = root
        while True:
            current_node_val = cur.val
            if current_node_val == val:
                return cur
            elif current_node_val < val:
                if cur.right is None:
                    return None
                cur = cur.right
                continue
            else:
                if cur.left is None:
                    return None
                cur = cur.left
                continue