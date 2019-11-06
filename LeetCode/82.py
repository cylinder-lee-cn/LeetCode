"""
82. 删除排序链表中的重复元素 II


给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:
输入: 1->2->3->3->4->4->5
输出: 1->2->5

示例 2:
输入: 1->1->1->2->3
输出: 2->3
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
        ahead = ListNode(None)
        newhead = ahead

        left = ListNode(None)

        while (head is not None):
            if (head.next is not None):
                if (head.val != left.val and head.val != head.next.val):
                    newhead.next = head
                    newhead = newhead.next
                left = head
                head = head.next
            else:
                if (head.val != left.val):
                    newhead.next = head
                else:
                    newhead.next = None
                head = head.next
        return ahead.next


ln0 = ListNode(1)
ln1 = ListNode(1)
ln2 = ListNode(2)
ln3 = ListNode(3)
ln4 = ListNode(3)
ln5 = ListNode(4)
ln6 = ListNode(4)
ln7 = ListNode(5)
ln8 = ListNode(5)

ln0.next = ln1
ln1.next = ln2
ln2.next = ln3
ln3.next = ln4
ln4.next = ln5
ln5.next = ln6
ln6.next = ln7
# ln7.next = ln8

s = Solution()
s.deleteDuplicates(ln0)
"""
此题解法：
* 要去除所有重复的元素，也就是说当指向链表的某个元素时，这个元素的左右两边的元素均不与它相同，就是需要的。
* 定义一个左元素left是ListNode(None)
* 遍历链表，将指向的元素与left和next进行比较，如果都不相同，就将新链表的next指向这个元素，反之仅仅取下一个
* 当走到链表末尾时(next is None)，仅和left比较，如果相同，就将next指向None，反之指向这个元素

"""
