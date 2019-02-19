'''
将两个有序链表合并为一个新的有序链表并返回。
新链表是通过拼接给定的两个链表的所有节点组成的。
'''


# Definition for singly-linked list.
class ListNode:
   def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1: return l2
        if not l2: return l1
        x = l1
        y = l2
        list_node = ListNode(0)
        while x and y:
            if x.val <= y.val :
                list_node.next = x
                x = x.next
            else:
                list_node.next = y
                y = y.next

            list_node = list_node.next
        if x.next ==None:
            list_node.next = y
        elif y.next == None:
            list_node.next = x
        return list_node