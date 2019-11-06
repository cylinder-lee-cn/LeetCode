"""
141. 环形链表

给定一个链表，判断链表中是否有环。
进阶：
你能否不使用额外空间解决此题？
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = head
        fast = head
        while (fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if (fast == slow):
                return True

        return False


"""
此题标准解法：使用快慢指针，快指针一次走2个，慢指针一次走1个，如果fast或fast.next是None，说明没有环，结束循环。
如果，fast==slow那么说明有环，结束循环。
"""
