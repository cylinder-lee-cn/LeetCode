"""
897. 递增顺序查找树

给定一个树，按中序遍历重新排列树，使树中最左边的结点现在是树的根，并且每个结点没有左子结点，只有一个右子结点。

示例 ：
输入：[5,3,6,2,4,null,8,1,null,null,null,7,9]

       5
      / \
    3    6
   / \    \
  2   4    8
 /        / \
1        7   9

输出：[1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

 1
  \
   2
    \
     3
      \
       4
        \
         5
          \
           6
            \
             7
              \
               8
                \
                 9

提示：
给定树中的结点数介于 1 和 100 之间。
每个结点都有一个从 0 到 1000 范围内的唯一整数值。
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.newNode = TreeNode(None)
        self.h = self.newNode

    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.inorderTraversalRecursion(root)
        # print(self.newNode.right.val)
        return self.newNode.right

    def inorderTraversalRecursion(self, root):
        if (root is not None):
            self.inorderTraversalRecursion(root.left)
            self.h.right = TreeNode(root.val)
            self.h = self.h.right
            # print(root.val)
            self.inorderTraversalRecursion(root.right)
        return


tn1 = TreeNode(5)
tn1l = TreeNode(3)
tn1r = TreeNode(6)
tn1ll = TreeNode(2)
tn1lr = TreeNode(4)
tn1lll = TreeNode(1)
tn1rr = TreeNode(8)
tn1rrl = TreeNode(7)
tn1rrr = TreeNode(9)

tn1.left = tn1l
tn1.right = tn1r
tn1l.left = tn1ll
tn1l.right = tn1lr
tn1ll.left = tn1lll
tn1r.right = tn1rr
tn1rr.left = tn1rrl
tn1rr.right = tn1rrr

s = Solution()
s.increasingBST(tn1)
"""
此题解法：
* 要求使用中序遍历
* 新建一个TreeNode作为root，然后在中序遍历的时候每次都给root增加一个right节点，并且将root指向root.right
"""
