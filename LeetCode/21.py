"""
21. 合并两个有序链表

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        tmphead = ListNode(0)
        l3 = tmphead

        while (l1 and l2):
            if (l1.val < l2.val):
                l3.next = l1
                l3 = l3.next
                l1 = l1.next
            else:
                l3.next = l2
                l3 = l3.next
                l2 = l2.next

        if (l1 is not None):
            l3.next = l1

        if (l2 is not None):
            l3.next = l2

        return tmphead.next


S = Solution()
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)
a1.next = a2
a2.next = a3

b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
b1.next = b2
b2.next = b3

p1 = (S.mergeTwoLists(a1, b1))

while (p1):
    print(p1.val)
    p1 = p1.next
"""
解题思路(部分参考网上):
* 如果任意一个链表为空,那么返回另外一个链表
* 创建一个链表头tmphead,作为新链表的开始
* 创建一个ListNode作为当前链表节点l3, 将tmphead赋给当前链表节点l3
* 比较l1和l2的val,将val小的链接到l3的next上, 并且指向链表的下一个值,同时也将l3.next指向当前节点,用于下一次的链接用
* 重复以上过程,直至l1或l2某个链表被遍历完
* 检查l1和l2,将非空的链表直接链在l3上.
  因为这是个有序的链表,其中某一个子链表被遍历完,说明另外一个链表剩下的都比已经链接的数字大,直接链接即可.
* 最后返回tmphead.next,就可以跳过自定义的链表头
"""
