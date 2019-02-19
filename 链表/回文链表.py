'''
请判断一个链表是否为回文链表。
'''

## 思路 判断一个链表是不是回文,第一:翻转查看是否一致
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ## 链表很需要判断 是否为空
        if not head:
            return None
        first = ListNode(0)
        first.next = head
        pre = None
        cur = head
        nxt = head.next
        while nxt:
            cur.next = pre
            pre = cur
            cur = nxt
            nxt = nxt.next
            cur.next = pre

        if cur == head:
            return True
        else:
            return False
