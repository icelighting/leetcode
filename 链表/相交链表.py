'''

编写一个程序，找到两个单链表相交的起始节点
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A = headA
        B = headB
        while headA.next:
            nxt1 = headA.next
            nxt1.next = headA
            headA = nxt1

        while headB.next:
            nxt2 = headB.next
            nxt2.next = headB
            headB = nxt2

        if headB == headA:
            return False
        while headA == headB:
            headA = headA.next
            headB = headB.next

        return headA
    ##超出时间限制
    def case2(self,headA, headB):
        while headA:
            headA = headA.next
        while headB:
            headB = headB.next
        if headB == headA:
            return True
        else:
            return False

    def case3(self, headA, headB):
        p1 = headA
        p2 = headB
        while p1 != p2:
            if p1.next == None:
                p1.next = headB
            if p2.next == None:
                p2.next = headA

            else:
                p1 = p1.next
                p2 = p2.next

        return p1
