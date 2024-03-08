from typing import Any, Iterable
from ArrayTree import ArrayTree, ArrayTreeNode


class SegmentTree(ArrayTree):
    r"""
    node -> sum/max/min of interval [s,e]
    if s==e : node is leaf
    else    : node.left  -> sum/max/min of interval [s,          (s+e)//2]
              node.right -> sum/max/min of interval [(s+e)//2+1, e       ]
    """

    def __init__(self, data: Iterable, merge=lambda x, y: x + y):
        super().__init__(size=4 * len(data))
        self.n = len(data)
        self.merge = merge
        if self.n > 0:
            self.build(data, self.root, 0, self.n - 1)

    def build(self, data: Iterable, node: ArrayTreeNode, s: int, e: int):
        if s == e:
            node.set(data[s],suppress_warninig=True)
        else:
            m = (s + e) // 2
            self.build(data, node.left, s, m)
            self.build(data, node.right, m + 1, e)
            node.set(self.merge(node.left.get(), node.right.get()),suppress_warninig=True)

    def change(self, index: int, val, node: ArrayTreeNode, s: int, e: int):
        if s == e:
            node.set(val)
        else:
            m = (s + e) // 2
            if index <= m:
                self.change(index, val, node.left, s, m)
            else:
                self.change(index, val, node.right, m + 1, e)
            node.set(self.merge(node.left.get(), node.right.get()))

    def update(self, index: int, val):
        self.change(index, val, self.root, 0, self.n - 1)

    def range(self, left: int, right: int, node: ArrayTreeNode, s: int, e: int) -> Any:
        if left == s and right == e:
            return node.get()
        m = (s + e) // 2
        if right <= m:
            return self.range(left, right, node.left, s, m)
        if left > m:
            return self.range(left, right, node.right, m + 1, e)
        return self.merge(
            self.range(left, m, node.left, s, m),
            self.range(m + 1, right, node.right, m + 1, e),
        )

    def sumRange(self, left: int, right: int) -> Any:
        return self.range(left, right, self.root, 0, self.n - 1)
