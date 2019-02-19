'''
给定一个链表，旋转链表，
将链表每个节点向右移动 k 个位置，
其中 k 是非负数。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        first = head
        count = 1
        while head.next != None:
            nxt = head.next
            head = nxt
            count += 1
        head.next = first
        s = 1
        while s< count-k+1:
            first = first.next
            s += 1
        knum = first.next
        first.next = None

        return knum