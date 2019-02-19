'''
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

说明：不允许修改给定的链表。

'''

'''
思路: 思路：按照上面的思路，假设两个指针在（图Z点）相遇，此时slow指针走过的路径是a+b，而fast指针走过的路径是a+b+c+b。
由于fast的步长是slow的两倍，因此可以得到：2（a+b）=a+b+c+b，解得a=c。
由上图可以看出从X点到Y点的距离与从Z点到Y点的距离相等，
即让slow指针与fast指针相遇后，我们让slow指针再指向头结点（X点），此时fast指针位置不变，
再让slow和fast指针同时后移，当两个指针相遇时，slow和fast指向的是恰好是环形链表的起始节点（Y点）

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return None
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast == None:
            return None
        slow = head
        while slow != fast and fast != None:  ##这里要防止,fast  后面是空的
            slow = slow.next
            fast = fast.next
        return fast

