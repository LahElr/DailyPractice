from typing import Iterable
import warnings
from BinaryTree import TreeNode

# for test:
# tree = ArrayTree(data=[3,5,1,6,2,0,8,None,None,7,4])


class ArrayTree:
    r'''
    A tree stored as an array.
    Use `ArrayTreeNode` as an inteface to navigate in the tree.
    '''
    def __init__(self, data: Iterable = None, tree: TreeNode = None, size=0):
        # if `data` is given, `tree` and `size` would be omitted
        # if `tree` is given, `size` would be omitted
        if data is not None:
            self.container = data
            self.size = len(self.container) - self.container.count(None)

        elif tree is not None:
            self.container = [None]
            self.size = 0

            def dfs(node, ptr):
                if len(self.container) <= ptr:
                    self.expand(ptr)
                self.container[ptr] = node.val
                self.size += 1
                if node.right is not None:
                    dfs(node.right, 2 * ptr + 2)
                if node.left is not None:
                    dfs(node.left, 2 * ptr + 1)

            dfs(tree, 0)

        elif size > 0:
            self.container = [None for _ in range(size)]
            self.size = 0

        else:
            self.container = [None]
            self.size = 0

    def __len__(self):
        return self.size

    def expand(self, ptr: int):
        self.container.extend([None for _ in range(ptr + 1 - len(self.container))])

    @property
    def root(self):
        return ArrayTreeNode(self, 0)

    def get_node(self, ptr):
        return ArrayTreeNode(self, ptr)

    def __str__(self):
        return f"ArrayTree object with {self.size} nodes and root value {self.container[0]}"

    def lfs(self):
        return list(filter(lambda x: x is not None, self.container))


class ArrayTreeNode:
    def __init__(self, tree: ArrayTree, ptr=0):
        self.ptr = ptr
        self.tree = tree

    def get(self):
        if len(self.tree.container) <= self.ptr:
            return None
        return self.tree.container[self.ptr]

    def set(self, val, suppress_warninig=False):
        if len(self.tree.container) <= self.ptr:
            self.tree.expand(self.ptr)
            prev_none_flag = True
        else:
            prev_none_flag = self.tree.container[self.ptr] is None

        if not suppress_warninig and self.tree.container[(self.ptr - 1) // 2] is None:
            warnings.warn("add an ArrayTree node with no effect parent", stacklevel=2)

        self.tree.container[self.ptr] = val

        if prev_none_flag and val is not None:
            self.tree.size += 1
        elif not prev_none_flag and val is None:
            self.tree.size -= 1
            if not suppress_warninig and (
                (
                    len(self.tree.container) > 2 * self.ptr + 1
                    and self.tree.container[2 * self.ptr + 1] is not None
                )
                or (
                    len(self.tree.container) > 2 * self.ptr + 2
                    and self.tree.container[2 * self.ptr + 2] is not None
                )
            ):
                warnings.warn(
                    "delete an ArrayTree node with effect child(ren)", stacklevel=2
                )

    @property
    def parent(self):
        return ArrayTreeNode(self.tree, (self.ptr - 1) // 2)

    @property
    def left(self):
        return ArrayTreeNode(self.tree, 2 * self.ptr + 1)

    @property
    def right(self):
        return ArrayTreeNode(self.tree, 2 * self.ptr + 2)

    def move_to_parent(self):
        self.ptr = (self.ptr - 1) // 2

    def move_to_left(self):
        self.ptr = 2 * self.ptr + 1

    def move_to_right(self):
        self.ptr = 2 * self.ptr + 2

    def __str__(self):
        return f"Node [{self.ptr}]->{self.get()} of {self.tree}"
