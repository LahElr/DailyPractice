r'''给定单链表的头节点 head ，
将所有索引为奇数的节点和索引为偶数的节点分别组合在一起，然后返回重新排序的列表。
第一个节点的索引被认为是 奇数 ， 第二个节点的索引为 偶数 ，以此类推。
请注意，偶数组和奇数组内部的相对顺序应该与输入时保持一致。
你必须在 O(1) 的额外空间复杂度和 O(n) 的时间复杂度下解决这个问题。
'''

#lahelr 如题所示分开即可

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)

data = [1,2,3,4,5]
t = ListNode()
n = None
for i in range(len(data)-1,-1,-1):
    t.val = data[i]
    t.next = n
    t,n = ListNode(),t

def printList(head):
    while head:
        print(f"{head.val}-> ",end="")
        head = head.next
    print()

def List2List(head):
    ret = []
    while head:
        ret.append(head.val)
        head = head.next
    return ret

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head or head.next is None:
            return head
        
        i = 1
        odd_list = None
        odd_list_head = None
        even_list = None
        even_list_head = None

        while head:
            next = head.next
            # print(head,next,i)
            if i%2 == 1:
                # add to odd list
                if odd_list is None:
                    odd_list = head
                    odd_list_head = head
                else:
                    odd_list.next = head
                    odd_list = head
                # printList(odd_list_head)
            else:
                if even_list is None:
                    even_list = head
                    even_list_head = head
                else:
                    even_list.next = head
                    even_list = head
                # printList(even_list_head)
            i+=1
            head = next
            continue
        
        odd_list.next = even_list_head
        even_list.next = None
        
        return odd_list_head


x = Solution()
printList(x.oddEvenList(n))