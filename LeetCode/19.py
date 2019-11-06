"""
19. 删除链表的倒数第N个节点

给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：
给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.

说明：
给定的 n 保证是有效的。

进阶：
你能尝试使用一趟扫描实现吗？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        fast = head
        slow = head

        # move n steps
        for i in range(n):
            fast = fast.next
        # if fast is None then remove the slow first element
        if (fast is None):
            return head.next

        while (fast.next is not None):
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

lt1 = ListNode(1)

s = Solution()
s.removeNthFromEnd(l1, 2)
s.removeNthFromEnd(lt1, 1)
"""
Hint 1:
Maintain two pointers and update one with a delay of n steps.

此题解法：
* 还是利用快慢指针的方式，快指针比慢指针先走n步。
* 当快指针走到末尾时，慢指针正好停在倒数第n+1个元素上
* 这时候只需要将慢指针的元素指向 自己.next.next 就

* 特殊情况是 fast走完n步以后已经走到链表的末尾了，就意味着是删除链表的第一个元素。

"""
