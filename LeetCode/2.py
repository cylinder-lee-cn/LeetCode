"""
2. 两数相加

给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(None)
        rl = head
        s = 0
        while (l1 is not None or l2 is not None):
            s = s // 10
            if (l1 is not None):
                s = s + l1.val
                l1 = l1.next

            if (l2 is not None):
                s = s + l2.val
                l2 = l2.next

            rl.next = ListNode(s % 10)
            rl = rl.next

        if (s >= 10):
            rl.next = ListNode(1)

        return head.next


# n1 = ListNode(2)
# n2 = ListNode(4)
# n3 = ListNode(3)
# n1.next = n2
# n2.next = n3

# m1 = ListNode(5)
# m2 = ListNode(6)
# m3 = ListNode(4)
# m1.next = m2
# m2.next = m3

n1 = ListNode(9)
n2 = ListNode(9)
n1.next = n2

m1 = ListNode(1)

s = Solution()
s.addTwoNumbers(n1, m1)

"""
此题解法：因为不知道两个链表的长度，所以使用while进行循环，只有当两个链表都指向None，才遍历完成。

用s存放两个链表val的和，使用s//10来获取进位，用s%10来获取个位数字。
当遍历完两个链表后检查一下s是否>=10，如果是，就必须再新链表上增补一位。
"""
