"""
102. 二叉树的层次遍历

给定一个二叉树，返回其按层次遍历的节点值。 （即逐层地，从左到右访问所有节点）。

例如:
给定二叉树: [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

返回其层次遍历结果：
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = [root]
        result = []

        while any(queue):
            tmp = []
            for i in range(len(queue)):
                node = queue.pop(0)
                tmp.append(node.val)

                if (node.left is not None):
                    queue.append(node.left)
                if (node.right is not None):
                    queue.append(node.right)

            result.append(tmp)

        return result


"""
此题解法：这是二叉树标准的广度搜索，标准解法是使用队列的方式来处理。

要注意，外部循环条件，不可以写成while queue:，因为当输入是[]，这个时候queue=[[]]，
python对这个结果的判定是True，这里可以使用while any(queue)

    3
   / \
  9  20
    /  \
   15   7

1、queue=[root(3)], 循环1次，queue弹出第一个元素，然后读取val，放入tmp里，tmp=[3]
    然后判断是否有左右节点，如果有依次将左右节点放入queue中
    queue=[[9]，[20]]，最后将tmp放入result中，result=[[3]]
2、继续循环queue，2次，依次弹出第一个元素，读取val，放入tmp，tmp=[9，20]
    再判断是否有左右节点，如果有将左右节点依次放入queue，将tmp加入result，result=[[3],[9,20]]
3、继续
"""
