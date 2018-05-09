# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        root = head
        l = []
        preNode = None
        while root != None:
            val = root.val
            if val in l:
                preNode.next = root.next
            else:
                l.append(val) 
                preNode = root
            root = root.next
        return l

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(2)
print Solution().deleteDuplicates(head)
while head != None:
    print head.val
    head = head.next