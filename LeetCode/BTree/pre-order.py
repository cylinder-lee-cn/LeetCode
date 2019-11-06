# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.result = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if (root is None):
            return self.result

        stack = []
        stack.append(root)
        while (len(stack) != 0):
            top = stack.pop()
            if (top.right is not None):
                stack.append(top.right)
            if (top.left is not None):
                stack.append(top.left)
            self.result.append(top.val)

        return self.result

    def preorderTraversalRecursion(self, root):
        if (root is not None):
            self.result.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

        return self.result


root = TreeNode(1)
l1 = TreeNode(2)
r = TreeNode(3)
ll = TreeNode(3)
lr = TreeNode(4)
rl = TreeNode(4)
rr = TreeNode(2)

root.left = l1
root.right = r
l1.left = ll
r.left = rr

s = Solution()

ret = s.preorderTraversal(root)
print(ret)

s.result.clear()
ret = s.preorderTraversal(root)
print(ret)

"""
前序遍历：先访问根节点，然后遍历左子树，最后是遍历右子树

此题解法：如果不用递归来进行二叉树遍历，就需要使用栈，首先将二叉树的根（root）放入栈，后续放入的顺序是右节点和左节点。
每次都弹出栈顶的元素用于内容的访问即可。

如果是递归的话就要在类里初始化一个返回值：

class Solution:
    def __init__(self):
        self.ret=[]

    def preorderTraversal(self, root):

        if (root is not None):
            self.ret.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)

        return self.ret

"""
