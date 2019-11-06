"""
98. 验证二叉搜索树

给定一个二叉树，判断其是否是一个有效的二叉搜索树。

假设一个二叉搜索树具有如下特征：

节点的左子树只包含小于当前节点的数。
节点的右子树只包含大于当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

示例 1:
输入:
    2
   / \
  1   3
输出: true

示例 2:
输入:
    5
   / \
  1   4
     / \
    3   6
输出: false
解释: 输入为: [5,1,4,null,null,3,6]。
     根节点的值为 5 ，但是其右子节点值为 4 。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def inorderTraversal(self, root):
        if (root is not None):
            self.inorderTraversal(root.left)
            self.result.append(root.val)
            self.inorderTraversal(root.right)

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.inorderTraversal(root)
        print(self.result)
        return self.result == sorted(self.result) and len(self.result) == len(
            set(self.result))


r1 = TreeNode(5)
r1l = TreeNode(1)
r1r = TreeNode(4)
r1rl = TreeNode(3)
r1rr = TreeNode(6)
r1.left = r1l
r1.right = r1r
r1r.left = r1rl
r1r.right = r1rr

s = Solution()
print(s.isValidBST(r1))
"""
此题解法：
* 所有左子树的值小于根节点，所有右子树的值大于根节点
* 根据这个特征，使用中序遍历，有效的二叉搜索树遍历后是个增序数组
* 只要遍历后的数组和排序后数组比较一下就知道
"""
