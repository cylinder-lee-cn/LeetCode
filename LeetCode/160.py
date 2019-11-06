"""
160. 相交链表

编写一个程序，找到两个单链表相交的起始节点。
例如，下面的两个链表：

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
在节点 c1 开始相交。

注意：
如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if (headA is None or headB is None):
            return None

        lenA = 1
        lenB = 1

        lnA = ListNode(None)
        lnB = ListNode(None)
        lnA = headA
        lnB = headB

        while (lnA.next is not None):
            lnA = lnA.next
            lenA = lenA + 1

        while (lnB.next is not None):
            lnB = lnB.next
            lenB = lenB + 1

        # print(lenA, lenB)

        if (lnA != lnB):
            return None

        diffstep = abs(lenA - lenB)

        lnA = headA
        lnB = headB

        if (lenA > lenB):
            for i in diffstep:
                lnA = lnA.next

        if (lenB > lenA):
            for i in range(diffstep):
                lnB = lnB.next

        while (lnA is not None and lnB is not None):
            if (lnA == lnB):
                return lnA
            else:
                lnA = lnA.next
                lnB = lnB.next

        return None


a1 = ListNode('a1')
a2 = ListNode('a2')
b1 = ListNode('b1')
b2 = ListNode('b2')
b3 = ListNode('b3')
c1 = ListNode('c1')
c2 = ListNode('c2')
c3 = ListNode('c3')
a1.next = a2
b1.next = b2
b2.next = b3
c1.next = c2
c2.next = c3
a2.next = c1
b3.next = c1

s = Solution()
print(s.getIntersectionNode(a1, b1))
"""
此题解法：

单链表的基础知识：
1、判断一个单链表是否存在环
用 两个指针代表快、慢指针，然后从头指针开始，快指针一次前进两个结点，慢指针一次前进一个结点，
则如果两个指针相遇（相等），则一定有环。若两指针不相遇，则 fast 指针遇到空指针后便结束循环。

2、若存在环，求环的长度
定理I： 两指针（fast和slow）从第一次碰撞点出发到第二次碰撞所走的长度即为环的长度。

3、若存在环，求环的入口（连接点）
定理II：第一次碰撞点到环的入口的距离，等于头指针到环的入口的距离。
因此，分别从头指针和碰撞点遍历链表，第一次相遇的点即为换的入口（连接点）。

4、如何判断链表相交，若相交则找到第一个交点
第一种情况：两个链表都不成环
思路1：将其中一个链表首尾相连，判断另一个链表是否存在环，如果存在，则两个链表相交，且找出来的环入口点即为相交的第一个点。
思路2：若如果两个不成环的链表相交，那么两个链表从相交点到尾结点都是相同的结点。
首先先遍历两个链表，记录下两个链表的长度（长链表a，短链表b）。
然后先让长链表移动a-b长度，然后两链表开始同步前进，相遇的第一个点即为环的第一个交点。

第二种情况：两个链表都成环
不可能的情况：一个有环，一个没有环
"""
