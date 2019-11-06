"""
148. 排序链表

在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        readhead = head
        tmpHead = ListNode(None)
        newHead = tmpHead

        lns = []
        while readhead is not None:
            lns.append((readhead.val, readhead))
            readhead = readhead.next
        lns.sort(key=lambda n: n[0])

        for ln in lns:
            tmpHead.next = ln[1]
            tmpHead = tmpHead.next
            tmpHead.next = None
        return newHead.next


ln1 = ListNode(4)
ln2 = ListNode(2)
ln3 = ListNode(1)
ln4 = ListNode(3)

ln1.next = ln2
ln2.next = ln3
ln3.next = ln4

s = Solution()
print(s.sortList(ln1))
"""
此题解法：
* 首先遍历原链表，将ListNode的val和对象的内存地址取出，以元组的形式存入List（不适用Dict是怕val有重复）
* 然后将List按照每个元素的val排序，排序使用到key=lambda n:n[0]，元组的第一位
* 再遍历List，依次将listnode的next指向下一个listnode

网友解法：
* 只将listnode的val取出，然后排序
* 遍历排序后的list，将原链表的val依次改为list的元素
* 这个解法实质上没有改变原链表内存地址的顺序，只是修改的内存地址的val

  listL = []
        p = cur = head
        while cur:
            listL.append(cur.val)
            cur = cur.next
        listL.sort()
        for i in listL:
            p.val = i
            p = p.next
        return head
"""
