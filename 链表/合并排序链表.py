'''
合并 k 个排序链表，
返回合并后的排序链表。
请分析和描述算法的复杂度。
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == []:
            return None
        link_Node = ListNode(0)
        first = link_Node
        while not lists:
            valList = [x[0].val for x in lists]
            k = len(lists)
            mimus = min(valList)
            mimus_index = valList.index(mimus)
            link_Node.next = lists[mimus_index][0]
            lists[mimus_index].pop(0)
            if [] in lists:
                lists.remove([])

        return first.next

