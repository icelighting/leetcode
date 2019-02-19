'''

在 O(n log n) 时间复杂度和常数级空间复杂度下，

对链表进行排序。
'''

# Definition for singly-linked list.
## 思路:归并排序,先找到中位点,在进行排序
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or  head.next == None:
            return head
        valList = []
        listNode =  ListNode(0)
        first = listNode
        while head:
            valList.append(valList)
        while valList:
            minus = min(valList)
            nxt = ListNode(minus)
            listNode.next = nxt
            listNode = nxt
            valList.remove(minus)

        return first.next

    def sortList1(self, head):
        if head is None or head.next is None:
            return None
        pre = head
        slow = head
        fast = head
        while fast is not None and fast.next is not None:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        ## 所以这里找到的slow 是链表的中位值
        pre.next = None
        return self.merge(self.sortList1(head), self.sortList1(slow))

    def merge(self, l1, l2):
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val <= l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l2.next, l1)
            return l2

    def sortList2(self, head):
        if head is None or head.next is None:
            return head
        pivot = head
        p = pivot
        l1 = ListNode(0)
        l2 = ListNode(0)

        s = l1
        f = l2
        tmp = head.next
        while tmp is not None:
            if tmp.val < pivot.val:
                s.next = tmp
                s = s.next
            elif tmp.val == pivot.val:
                p.next = tmp
                p = p.next
            else:
                f.next = tmp
                f = f.next
            tmp = tmp.next
        s.next = None
        f.next = None
        p.next = None
        l3 = self.sortList2(l1.next)
        l4 = self.sortList2(l2.next)
        if l3 is not None:
            l5 = l3
            while l5.next is not None:
                l5 = l5.next
            l5.next = pivot
            p.next = l4
            return l3
        else:
            p.next = l4
        return pivot

        #  # 实现逻辑: 采用归并排序，先分后合并
        # self.merge_sort()

    def sortList3(self, head):
            #         cur = head
            #         lit = []
            #         while cur:
            #             lit.append(cur.val)
            #             cur = cur.next

            #         lit = sorted(lit)    # sorted()
            #         print(lit)
            #         pre= ListNode(0)
            #         prep = pre
            #         for i in lit:
            #             #prep.val = lit[i]
            #             prep.next = ListNode(i)
            #             prep = prep.next
            #         return pre.next
            cur = head
            if cur == None or cur.next == None:
                return head
            a = []
            while cur:
                a.append(cur.val)
                cur = cur.next
            a = sorted(a)

            cur = head
            for i in a:
                cur.val = i
                cur = cur.next
            return head