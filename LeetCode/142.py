"""
142. 环形链表 II

给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

说明：不允许修改给定的链表。

进阶：
你是否可以不用额外空间解决此题？

"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head

        while (fast is not None and fast.next is not None):
            fast = fast.next.next
            slow = slow.next
            if (fast == slow):
                fast = head
                while (fast != slow):
                    fast = fast.next
                    slow = slow.next
                return slow
        return None


"""
此题解法：
* 首先判断是否有环，就使用快慢指针，快指针一次走2，慢指针一次走1，两针相遇，说明有环。
* 找到入环的第一个节点，就是当两针相遇后，将快指针拨回链表开头，然后两针都每次走1，相遇的地方就是环的入口
"""
