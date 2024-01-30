from collections import deque
import utils


class TreeNode:
    def __init__(self, x=None, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __str__(self):
        return f"<BinaryTree.TreeNode object at {id(self)}, with left {self.left.val if self.left is not None else None} and right {self.right.val if self.right is not None else None}.>"


def build_tree(data):
    if len(data) == 0:
        return None
    data = deque(data)
    root = TreeNode(data.popleft())
    node_queue = deque([root])
    while node_queue and data:
        cur = node_queue.popleft()
        if cur is None:
            continue
        v = data.popleft()
        if v is not None:
            cur.left = TreeNode(v)
        else:
            cur.left = None
        node_queue.append(cur.left)
        if len(data) > 0:
            v = data.popleft()
            if v:
                cur.right = TreeNode(v)
            else:
                cur.right = None
            node_queue.append(cur.right)
        else:
            cur.right = None
    return root


def search_in_tree(root, v):
    r"""
    ! not BST search
    """
    #! not BST search
    if root is None:
        return None
    if root.val == v:
        return root
    left_result = search_in_tree(root.left, v)
    if left_result is not None:
        return left_result
    right_result = search_in_tree(root.right, v)
    if right_result is not None:
        return right_result
    return None

def lfs(root,action=None, process_none=False):
    queue = deque([root])
    while queue:
        cur = queue.popleft()
        if cur is not None:
            if action is not None:
                action(cur)
            queue.append(cur.left)
            queue.append(cur.right)
        elif process_none:
            if action is not None:
                action(cur)
    return

def lfs_tree(root):
    ret = []
    def action(node):
        nonlocal ret
        ret.append(node.val if node is not None else None)
    lfs(root,action,True)
    return remove_tail_none(ret)

@utils.deprecated
def __lfs_tree(root):
    queue = deque([root])
    ans = []
    while queue:
        cur = queue.popleft()
        if cur is None:
            ans.append(None)
            continue
        ans.append(cur.val)
        queue.append(cur.left)
        queue.append(cur.right)
    return remove_tail_none(ans)


def remove_tail_none(ls):
    for i in range(len(ls) - 1, -2, -1):
        if i == -1 or ls[i] is not None:
            break
    return ls[: i + 1]


def split_lfs(self, root):
    if root is None:
        return []

    queue = deque([root, None])
    ans = [[]]
    while True:
        cur = queue.popleft()
        if cur is None:
            ans.append([])
            if len(queue) > 0:
                queue.append(None)
                continue
            else:
                break
        ans[-1].append(cur.val)
        if cur.left is not None:
            queue.append(cur.left)
        if cur.right is not None:
            queue.append(cur.right)
    return ans[:-1]


def dfs_tree(root, mode="pre", process_none=False):
    r'''
    A demo how function `dfs` is used.
    '''
    ret = []

    def action(node: TreeNode):
        nonlocal ret
        ret.append(node.val)

    dfs(root, action, ["pre", "in", "post"].index(mode), process_none)
    return ret


def dfs(root, action=None, mode=0, process_none=False):
    if root is not None:
        if mode == 0:
            if action is not None:
                action(root)
            dfs(root.left, action, mode, process_none)
            dfs(root.right, action, mode, process_none)
            return
        if mode == 1:
            dfs(root.left, action, mode, process_none)
            if action is not None:
                action(root)
            dfs(root.right, action, mode, process_none)
            return
        if mode == 2:
            dfs(root.left, action, mode, process_none)
            dfs(root.right, action, mode, process_none)
            if action is not None:
                action(root)
            return
    elif process_none:
        if action is not None:
            action(root)
