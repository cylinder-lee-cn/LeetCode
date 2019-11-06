"""
876. 链表的中间结点

给定一个带有头结点 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。


示例 1：

输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
示例 2：

输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。

提示：

给定链表的结点数介于 1 和 100 之间。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        chain_i = head
        chain_j = head
        while 1:
            if (chain_j.next is None):
                return chain_i
            if (chain_j.next.next is None):
                return chain_i.next
            chain_i = chain_i.next
            chain_j = chain_j.next.next


l1 = ListNode(1)
l2 = ListNode(2)
l3 = ListNode(3)
l4 = ListNode(4)
l5 = ListNode(5)
l6 = ListNode(6)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5
l5.next = l6

s = Solution()
# print(s.middleNode(l1), l1.val)
print(s.middleNode(l1))
"""
此题解法：找链表的中心点，最标准就是使用’快、慢‘指针，慢指针一次走一位，快指针一次走两位。
* 当快指针走到尾部时，慢指针正好走了一半。
* 快指针走到尾部的含义是 快.next is None 或者是 快.next.next is None
* 如果是偶数个元素，中间其实指的是中间2个元素，慢指针正好停在前一个，如果要后一个的话就取 慢.next

"""
