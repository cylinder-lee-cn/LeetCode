"""
155. 最小栈

设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。

push(x) -- 将元素 x 推入栈中。
pop() -- 删除栈顶的元素。
top() -- 获取栈顶元素。
getMin() -- 检索栈中的最小元素。
示例:

MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> 返回 -3.
minStack.pop();
minStack.top();      --> 返回 0.
minStack.getMin();   --> 返回 -2.

"""


class MinStack:
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.minstack = []
        self.minitem = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.minstack.append(x)
        if (self.minitem is None or self.minitem > x):
            self.minitem = x

    def pop(self):
        """
        :rtype: void
        """
        self.minstack.pop()

        self.minitem = None
        for n in self.minstack:
            if (self.minitem is None or n < self.minitem):
                self.minitem = n

    def top(self):
        """
        :rtype: int
        """
        return self.minstack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minitem


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())

"""
此题解法：下方网友的解法很巧妙，典型的空间换时间的方式。

定义了两个list，一个作为普通的Stack，按顺序存放数字。同时定义了一个存放当前最小值的Stack与普通栈的元素进行对应。

当push(-2)
数据栈[-2]
最小栈[-2]
当push(0)
数据栈[-2,0]
最小栈[-2,-2]
当push(-3)
数据栈[-2,0,-3]
最小栈[-2,-2,-3]
当push(1)
数据栈[-2,0,-3,1]
最小栈[-2,-2,-3,-3]

当进行push操作时，如果x小于minstack[-1]，就minstack.append(x)，否则就再把minstack[-1]添加一遍。

也就是最小栈中的元素永远对应数据栈当前元素的最小值，当getMin()时只需要访问最小栈的末尾元素 minstack[-1]

当数据栈进行操作pop()，最小栈也同时进行pop()即可，就能保证最小值和数据值的对应关系。

class MinStack:
    def __init__(self):

        self.stack = []   # 数据栈
        self.minVal = []   # 最小值栈
        # self.size = 0

    def push(self, x):

        self.stack.append(x)  # push元素
        if len(self.minVal) == 0:
            self.minVal.append(x)
        else:
            if (x > self.minVal[-1]): # x要大于最小值栈的栈顶元素，不加入
                x = self.minVal[-1]
            self.minVal.append(x)     # 否则
        # self.size += 1

    def pop(self):

         # 是否有必要加条件：长度>0？看来是没有必要。因为一定是先push再pop
        self.minVal.pop()
        self.stack.pop()

    def top(self):

        return self.stack[-1]

    def getMin(self):

        return self.minVal[-1]
"""
