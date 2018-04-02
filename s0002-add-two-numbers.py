class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        tmp = []
        node = None
        flag = 0
        while(l1 and l2):
            val = l1.val + l2.val + flag
            flag = val / 10
            node = ListNode(val % 10)
            tmp.append(val % 10)
            node = node.next
            l1 = l1.next
            l2 = l2.next
        while(l1):
            val = l1.val + flag
            flag = val / 10
            node = ListNode(val % 10)
            tmp.append(val % 10)
            node = node.next
            l1 = l1.next
        while(l2):
            val = l2.val + flag
            flag = val / 10
            node = ListNode(val % 10)
            tmp.append(val % 10)
            node = node.next
            l2 = l2.next
        if(flag):
            tmp.append(flag)
        return tmp
