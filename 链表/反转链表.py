'''
反转一个单链表。
'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        cur = head
        pre = None
        nxt = cur.next
        while nxt:##采用倒装的方式将链表重新排列,去一个放在末尾,再往前排
            cur.next = pre
            pre = cur
            cur = nxt
            nxt = nxt.next
            cur.next = pre
            head = cur
        return head

    def case2(self, head):## 采用列表列出 节点  在反转
        if not head:
            return head
        first = head
        l =[]
        while head:
            l.append(head)
            head = head.next
        for i in range(len(l) - 1):
            l[::-1][i].next = l[::-1][i + 1]

        l[0].next = None
        return l[::-1][0]
