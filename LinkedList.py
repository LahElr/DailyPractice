class LinkedListNode(object):
    def __init__(self, val=None, next=None, before=None):
        self.val = val
        self.next = next
        self.before = before

    def __str__(self):
        return f"LinkedListNode with value {self.val}, between {self.before.val if self.before else None} and {self.next.val if self.next else None}"


class LinkedList(object):
    def __init__(self, data=None):
        if data is None or len(data) == 0:
            self.head = None
            self.length = 0
            self.tail = None
        else:
            self.head = LinkedListNode(data[0])
            self.length = len(data)
            if len(data) >= 1:
                cur = self.head
                for d in data[1:]:
                    cur.next = LinkedListNode(val=d, before=cur)
                    self.tail = cur
                    cur = cur.next

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
            return
        self.tail.next = LinkedListNode(val=val, before=self.tail)
        self.tail = self.tail.next
        self.length += 1

    def add_start(self, val):
        if self.length == 0:
            self.head = self.tail = LinkedListNode(val)
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
