"""
237. 删除链表中的节点

请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:

    4 -> 5 -> 1 -> 9
示例 1:
输入: head = [4,5,1,9], node = 5
输出: [4,1,9]
解释: 给定你链表中值为 5 的第二个节点，那么在调用了你的函数之后，该链表应变为 4 -> 1 -> 9.

示例 2:
输入: head = [4,5,1,9], node = 1
输出: [4,5,9]
解释: 给定你链表中值为 1 的第三个节点，那么在调用了你的函数之后，该链表应变为 4 -> 5 -> 9.

说明:
链表至少包含两个节点。
链表中所有节点的值都是唯一的。
给定的节点为非末尾节点并且一定是链表中的一个有效节点。
不要从你的函数中返回任何结果。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


"""
此题解法：此题名为删除，其实是借用删除的说法。链表只能单向访问，题中的node是指链表中要删除的一个node。
本质上是无法删除node的，只是改变node的指向和val。而且题中有严格的约束条件（见题的说明）
[4，5，1，9] node=5，如果要将node5去掉，其实是将node5的val改变成node5.next的val
也就是 node.val=node.next.val，就会变成[4，1，1，9]，然后将node5的next指向跳过1项
node.next=node.next.next，本来node5的next是指向第3个1，现在就指向了9，就变成了[4，1，9]
"""
