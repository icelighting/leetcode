'''

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（
索引从 0 开始）。
如果 pos 是 -1，则在该链表中没有环。
'''


'''
思路思路：
这里给定两个指针，fast和slow。
两个指针同时从头结点开始出发，fast指针走两步，slow指针走一步；
若链表有环，这两个指针肯定会在某点相遇；若链表无环，fast会直接先到达NULL。
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False
