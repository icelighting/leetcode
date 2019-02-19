'''
给出两个 非空 的链表用来表示两个非负的整数。
其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

'''

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        nxt1 = l1.next
        nxt2 = l2.next
        cur = l1
        while nxt1.next or nxt2.next :
            if nxt1.next == None:
                nxt1.next = ListNode(0)
            if nxt2.next == None:
                nxt2.next = ListNode(0)
            cur.val = nxt1.val + nxt2.val
            nxt1 = nxt1.next
            nxt2 = nxt2.next
            nxt = cur.next
            if cur.val >= 10:
                cur.val = cur.val %10
                nxt.val = nxt1.val + nxt2.val +1
            cur = nxt


        return l1

    def case2(self,l1, l2):
        val_sum = l1.val + l2.val
        list_node = ListNode(val_sum % 10)
        a = val_sum // 10
        node = list_node
        while True:
            try:
                l1 = l1.next
            except:
                pass
            try:
                l2 = l2.next
            except:
                pass
            if not l1 and not l2:
                break
            elif not l1:
                l1_val = 0
                l2_val = l2.val
            elif not l2:
                l2_val = 0
                l1_val = l1.val
            else:
                l1_val = l1.val
                l2_val = l2.val
            val_sum = l1_val + l2_val + a
            temp_node = ListNode(val_sum % 10)
            node.next = temp_node
            node = temp_node
            a = val_sum // 10
        if a != 0:
            node.next = ListNode(a)
        return list_node