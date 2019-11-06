"""
206. 反转链表

反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if (head is None or head.next is None):
            return head

        pre=None
        cur=head
        newhead=cur

        while cur:
            newhead=cur
            tmp=cur.next
            cur.next=pre
            pre=cur
            cur=tmp
        return newhead

l1=ListNode(1)
l2=ListNode(2)
l3=ListNode(3)
l4=ListNode(4)
l5=ListNode(5)
l1.next=l2
l2.next=l3
l3.next=l4
l4.next=l5

s=Solution()
p=s.reverseList(l1)

while p:
    print(p.val)
    p=p.next

"""
循环的方法中，使用pre指向前一个结点，cur指向当前结点，每次把cur->next指向pre即可。
"""