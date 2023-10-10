from collections import deque


class TreeNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

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
        if v:
            cur.left = TreeNode(v)
        else:
            cur.left = None
        node_queue.append(cur.left)
        if len(data)>0:
            v = data.popleft()
            if v:
                cur.right = TreeNode(v)
            else:
                cur.right = None
            node_queue.append(cur.right)
        else:
            cur.right = None
    return root

def search_in_tree(root,v):
    #! not BST search
    if root is None:
        return None
    if root.val == v:
        return root
    left_result = search_in_tree(root.left,v)
    if left_result is not None:
        return left_result
    right_result = search_in_tree(root.right,v)
    if right_result is not None:
        return right_result
    return None

def lfs_tree(root):
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
    for i in range(len(ls)-1,-2,-1):
        if i == -1 or ls[i] is not None:
            break
    return ls[:i+1]