r"""层序遍历并返回层内元素和最大的几层
"""

# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        stack = collections.deque([root, 0])
        current_layer_sum = 0
        max_layer_sum = -float("inf")
        max_layer_pos = 0
        current_layer_pos = 0
        while stack:
            cur = stack.popleft()
            if cur == 0:
                current_layer_pos += 1
                if current_layer_sum > max_layer_sum:
                    max_layer_sum = current_layer_sum
                    max_layer_pos = current_layer_pos
                if len(stack) == 0:
                    break
                current_layer_sum = 0
                stack.append(0)
                continue
            if cur is None:
                continue
            current_layer_sum += cur.val
            if cur.left:
                stack.append(cur.left)
            if cur.right:
                stack.append(cur.right)
        return max_layer_pos


root = TreeNode(1, 
        left=TreeNode(7, 
            left=TreeNode(7), 
            right=TreeNode(-8)), 
        right=TreeNode(0)
)

print(Solution().maxLevelSum(root))
