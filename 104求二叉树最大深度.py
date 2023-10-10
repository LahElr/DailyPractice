from collections import deque
from typing import Optional
from BinaryTree import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        queue = deque([(root, 1)])
        ret = 1
        while queue:
            cur, height = queue.popleft()
            ret = max(height, ret)
            if cur.left:
                queue.append((cur.left, height + 1))
            if cur.right:
                queue.append((cur.right, height + 1))
        return ret
