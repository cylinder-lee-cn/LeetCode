"""
328. 奇偶链表

给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。
请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL

示例 2:
输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL

说明:
应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # only 1 or 2 elements, retrun head
        if (head is None or head.next is None or head.next.next is None):
            return head

        i = 1
        odd = ListNode(None)
        oddtmp = odd
        even = ListNode(None)
        eventmp = even
        while (head is not None):
            if (i % 2 == 1):
                oddtmp.next = head
                oddtmp = oddtmp.next
            else:
                eventmp.next = head
                eventmp = eventmp.next
            i = i + 1
            head = head.next

        eventmp.next = None
        oddtmp.next = even.next
        return odd.next


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

t1 = ListNode(None)

s = Solution()
s.oddEvenList(l1)
print(s.oddEvenList(t1))
"""
此题解法：
使用一个计数器，从1开始，每获取一个head的元素就+1，根据计数器的数值来判断是奇数还是偶数节点。

分别将奇数节点和偶数节点链接到临时的odd和even节点上。
最后将even节点链接到odd节点上。别忘了将even最后的next设置成None
"""
