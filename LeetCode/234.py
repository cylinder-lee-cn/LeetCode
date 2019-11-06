"""
234. 回文链表

请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        hl = []
        while (head):
            hl.append(head.val)
            head = head.next

        if (hl == hl[::-1]):
            return True
        else:
            return False


#         if (head is None or head.next is None):
#             return True

#         lat = head.next
#         pre = head

#         # 切分成lat和pre两个子链表
#         while (lat is not None and lat.next is not None):
#             lat = lat.next.next
#             pre = pre.next

#         # 翻转pre链表
#         cur = pre.next
#         pre.next = None
#         p = None
#         while (cur is not None):
#             tmp = cur.next
#             cur.next = p
#             p = cur
#             cur = tmp

#         # 比较两个子链表
#         while (p is not None and head is not None):
#             if (p.val is not head.val):
#                 return False
#             p = p.next
#             head = head.next

#         return True

# """
# 标准解法：找到链表的中间，分成两个子链表，反转其中一个，
# 然后顺序比较两个子链表的val，如果都相同就是回文链表。

# * 使用快慢指针的方法可以将一个链表分成两个链表，
#   快指针每次走两步，慢指针每次走一步，快指针走到头的时候，慢指针正好走了一半
# * 反转链表的方式是206题中的标准解法
# """
