# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        t1 = self.getList(l1)
        t2 = self.getList(l2)
        t2.extend(t1)
        t2.sort()
        return t2
    
    def getList(self, node):
        l = []
        while(node):
            l.append(node.val)
            node = node.next
        return l
