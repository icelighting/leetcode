'''
给定一个链表，
删除链表的倒数第 n 个节点，
并且返回链表的头结点。
'''
#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0
        headL = []
        while head != None:
            headL.append(head)
            head = head.next
            count += 1
        if count == 1:
            return None
        if n == count:
            return headL[0].next
        if headL[-n].next == None:
            headL[-n - 1].next = None
        else:
            headL[-n - 1].next = headL[-n + 1]
        return headL[0]

    # 对链表进行一次扫描,设置两个同样的指针p,q,p指针先走k=n步, q指针再接着走 当p走到尾的时候,q刚好在尾部倒数第n个节点地方
    def case2(self,head, n):
        pre = ListNode(0)
        pre.next = head
        p = q = pre
        for i in range(n):
            p = p .next
        first = q
        while p.next:
            p = p.next
            q = q.next
        q.next = q.next.next
        return first

