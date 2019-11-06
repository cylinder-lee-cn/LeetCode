"""
83. 删除排序链表中的重复元素

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:
输入: 1->1->2
输出: 1->2

示例 2:
输入: 1->1->2->3->3
输出: 1->2->3
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head == None):
            return None

        newhead = ListNode(head.val)
        nowl = newhead

        while (head != None):
            if (nowl.val != head.val):
                nowl.next = head
                nowl = nowl.next
            head = head.next
            nowl.next = None
        return newhead

s = Solution()

# a1 = ListNode(1)
# a2 = ListNode(1)
# a3 = ListNode(2)
# a1.next = a2
# a2.next = a3
#
# r1 = s.deleteDuplicates(a1)
# while (r1):
#     print(r1.val)
#     r1 = r1.next

b1 = ListNode(1)
b2 = ListNode(1)
b3 = ListNode(2)
b4 = ListNode(3)
b5 = ListNode(3)
b1.next = b2
b2.next = b3
b3.next = b4
b4.next = b5

r2 = s.deleteDuplicates(b1)
while (r2):
    print(r2.val)
    r2 = r2.next
