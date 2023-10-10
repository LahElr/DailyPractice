# Definition for a binary tree node.
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # lahelr 每层的最后一个
        # lahelr 层序遍历
        ans = {}
        max_depth = -1
        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()
            if node:
                max_depth = max(depth, max_depth)
                ans[depth] = node.val
                queue.append((node.left, depth + 1))
                queue.append((node.right, depth + 1))
        return [ans[d] for d in range(max_depth + 1)]


tree = TreeNode(
    1,
    left=(TreeNode(2, left=None, right=TreeNode(5))),
    right=(TreeNode(3, left=None, right=TreeNode(4))),
)
print(Solution().rightSideView(tree))
