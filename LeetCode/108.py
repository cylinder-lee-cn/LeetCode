"""
108. 将有序数组转换为二叉搜索树

将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过1。

示例:
给定有序数组: [-10,-3,0,5,9],
一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
      0
     / \
   -3   9
   /   /
 -10  5

基础知识：
二叉查找树（英语：Binary Search Tree），也称为二叉搜索树、有序二叉树（ordered binary tree）
或排序二叉树（sorted binary tree），是指一棵空树或者具有下列性质的二叉树：

* 若任意节点的左子树不空，则左子树上所有节点的值均小于它的根节点的值；
* 若任意节点的右子树不空，则右子树上所有节点的值均大于它的根节点的值；
* 任意节点的左、右子树也分别为二叉查找树；
* 没有键值相等的节点。

二叉查找树相比于其他数据结构的优势在于查找、插入的时间复杂度较低。为 O(log n)。
二叉查找树是基础性数据结构，用于构建更为抽象的数据结构，如集合、multiset、关联数组等。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def _sortedArrayToBST(self, nums, start, end):
        if start > end:
            return None

        mid = (end - start) // 2 + start
        midNode = TreeNode(nums[mid])
        midNode.left = self._sortedArrayToBST(nums, start, mid - 1)
        midNode.right = self._sortedArrayToBST(nums, mid + 1, end)
        return midNode

    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self._sortedArrayToBST(nums, 0, len(nums) - 1)


s = Solution()
s.sortedArrayToBST([-10, -3, 0, 5, 9])
