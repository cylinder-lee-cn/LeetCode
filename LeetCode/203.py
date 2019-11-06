"""
203. 删除链表中的节点

删除链表中等于给定值 val 的所有节点。

示例:
输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5

"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """

        tmphead = ListNode(0)
        l=tmphead

        while (head):
            if (head.val != val):
                l.next = head
                l = l.next
            head = head.next
            l.next=None

        return tmphead.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(6)
l4 = ListNode(3)
l5 = ListNode(4)
l6 = ListNode(5)
l7 = ListNode(6)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6
l6.next = l7

s = Solution()
print(s.removeElements(l1, 6))
