from copy import deepcopy
from typing import Iterable, Union


class LinkedListNode(object):
    def __init__(self, val=None, next=None, before=None):
        self.val = val
        self.next = next
        self.before = before

    def __str__(self):
        return f"LinkedListNode with value {self.val}, between {self.before.val if self.before else None} and {self.next.val if self.next else None}"


class LinkedList(object):
    def __init__(self, data: Union[Iterable, LinkedListNode] = None):
        # assert hasattr(data,"__getitem__") or isinstance(data,LinkedList) or isinstance(data,LinkedListNode)
        if data is None or (hasattr(data, "__len__") and len(data) == 0):
            self.head = None
            self.length = 0
            self.tail = None
        elif hasattr(data, "__getitem__"):
            self.head = LinkedListNode(data[0])
            self.length = len(data)
            if len(data) >= 1:
                cur = self.head
                for d in data[1:]:
                    cur.next = LinkedListNode(val=d, before=cur)
                    self.tail = cur.next
                    cur = cur.next
        elif isinstance(data, LinkedList):
            self.head = None
            self.length = 0
            self.tail = None
            cur = data.head
            while cur is not None:
                self.add_end(cur.val)
                cur = cur.next
        elif isinstance(data, LinkedListNode):
            self.head = None
            self.length = 0
            self.tail = None
            cur = data
            while cur is not None:
                self.add_end(cur.val)
                cur = cur.next
        else:
            raise TypeError(
                f"Unexpected object {data} of type {type(data)}", stacklevel=2
            )

    def to_list(self):
        if self.length == 0:
            return []
        ret = []
        cur = self.head
        while cur:
            ret.append(cur.val)
            cur = cur.next
        return ret

    def __str__(self):
        return " ->".join(map(str, self.to_list()))

    def __len__(self):
        return self.length

    def __sizeof__(self):
        return self.length

    def pop_head(self):
        assert self.head
        ret = self.head.val
        self.head = self.head.next
        self.length -= 1
        return ret

    def pop_end(self):
        assert self.tail
        ret = self.tail.val
        self.tail = self.tail.before
        self.length -= 1
        return ret

    def add_end(self, val):
        if self.length == 0:
            self.head = self.tail = LinkedListNode(val)
            self.length += 1
            return
        self.tail.next = LinkedListNode(val=val, before=self.tail)
        self.tail = self.tail.next
        self.length += 1

    def add_start(self, val):
        if self.length == 0:
            self.head = self.tail = LinkedListNode(val)
            self.length += 1
            return
        self.head.before = LinkedListNode(val=val, next=self.head)
        self.head = self.head.before
        self.length += 1

    def get_ith(self, i):
        if i >= self.length:
            raise IndexError
        cur = self.head
        j = 0
        while cur:
            if j == i or j >= self.length:
                return cur.val
            cur = cur.next
            j += 1

    def get_ith_pointer(self, i):
        if i >= self.length:
            raise IndexError
        cur = self.head
        j = 0
        while cur:
            if j == i or j >= self.length:
                return cur
            cur = cur.next
            j += 1

    def delete_ith(self, i):
        if i >= self.length:
            raise IndexError
        cur = self.head
        j = 0
        if i == 0:
            self.pop_head()
            return
        if i == self.length - 1:
            self.pop_end()
            return
        while cur:
            if j == i:
                before = cur.before
                next = cur.next
                before.next = next
                next.before = before
                return
            cur = cur.next
            j += 1

    def pop_ith(self, i):
        if i >= self.length:
            raise IndexError
        cur = self.head
        j = 0
        if i == 0:
            return self.pop_head()
        if i == self.length - 1:
            return self.pop_end()
        while cur:
            if j == i:
                before = cur.before
                next = cur.next
                before.next = next
                next.before = before
                return cur.val
            cur = cur.next
            j += 1

    def reverse(self):
        if self.length <= 1:
            return
        self.head, self.tail = self.tail, self.head
        cur = self.head
        while True:
            if cur is None:
                return
            cur.next, cur.before = cur.before, cur.next
            cur = cur.next

    def sort(self, reversed=False):
        # this is qsort
        if self.length <= 1:
            return
        elif self.length == 2:
            a = self.head.val
            b = self.tail.val
            self.head.val = min(a, b)
            self.tail.val = max(a, b)
            return

        stack = [(self.head, self.tail)]
        while stack:
            left_node, right_node = stack.pop()
            if right_node == left_node.next:
                a = left_node.val
                b = right_node.val
                left_node.val = min(a, b)
                right_node.val = max(a, b)
            else:
                split_val = left_node.val
                left_ptr = left_node
                right_ptr = right_node
                move_right = True
                while True:
                    if left_ptr == right_ptr:
                        break
                    if move_right:
                        if right_ptr.val < split_val:
                            left_ptr.val = right_ptr.val
                            left_ptr = left_ptr.next
                            move_right = False
                        else:
                            right_ptr = right_ptr.before
                    else:
                        if left_ptr.val > split_val:
                            right_ptr.val = left_ptr.val
                            right_ptr = right_ptr.before
                            move_right = True
                        else:
                            left_ptr = left_ptr.next
                left_ptr.val = split_val

                if left_node != left_ptr:
                    stack.append((left_node, left_ptr.before))
                if right_node != right_ptr:
                    stack.append((right_ptr.next, right_node))

        if reversed:
            self.reverse()
        return


def merge_ordered_lists(list1: LinkedList, list2: LinkedList) -> LinkedList:
    # 将两个升序链表合并为一个新的 升序 链表并返回
    if list1 is None:
        return deepcopy(list2)
    if list2 is None:
        return deepcopy(list1)

    ret = LinkedList()
    ptr1 = list1.head
    ptr2 = list2.head

    while True:
        if ptr1 is None and ptr2 is None:
            return ret
        a = float("inf") if ptr1 is None else ptr1.val
        b = float("inf") if ptr2 is None else ptr2.val
        if a < b:
            ret.add_end(a)
            ptr1 = ptr1.next
        else:
            ret.add_end(b)
            ptr2 = ptr2.next
