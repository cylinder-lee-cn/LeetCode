"""
622. 设计循环队列

设计你的循环队列实现。 循环队列是一种线性数据结构，其操作表现基于 FIFO（先进先出）原则并且队尾被连接在队首之后以形成一个循环。
它也被称为“环形缓冲器”。循环队列的一个好处是我们可以利用这个队列之前用过的空间。
在一个普通队列里，一旦一个队列满了，我们就不能插入下一个元素，即使在队列前面仍有空间。
但是使用循环队列，我们能使用这些空间去存储新的值。
你的实现应该支持如下操作：

MyCircularQueue(k): 构造器，设置队列长度为 k 。
Front: 从队首获取元素。如果队列为空，返回 -1 。
Rear: 获取队尾元素。如果队列为空，返回 -1 。
enQueue(value): 向循环队列插入一个元素。如果成功插入则返回真。
deQueue(): 从循环队列中删除一个元素。如果成功删除则返回真。
isEmpty(): 检查循环队列是否为空。
isFull(): 检查循环队列是否已满。

示例：
MyCircularQueue circularQueue = new MycircularQueue(3); // 设置长度为3

circularQueue.enQueue(1);  // 返回true

circularQueue.enQueue(2);  // 返回true

circularQueue.enQueue(3);  // 返回true

circularQueue.enQueue(4);  // 返回false,队列已满

circularQueue.Rear();  // 返回3

circularQueue.isFull();  // 返回true

circularQueue.deQueue();  // 返回true

circularQueue.enQueue(4);  // 返回true

circularQueue.Rear();  // 返回4

提示：
所有的值都在 1 至 1000 的范围内；
操作数将在 1 至 1000 的范围内；
请不要使用内置的队列库。
"""


class MyCircularQueue:
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.maxlen = k
        self.queue = []

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if (len(self.queue) >= self.maxlen):
            return False
        else:
            self.queue.append(value)
            return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if (len(self.queue) >= 1):
            self.queue.pop(0)
            return True
        else:
            return False

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if (len(self.queue) >= 1):
            return self.queue[0]
        else:
            return -1

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if (len(self.queue) >= 1):
            return self.queue[-1]
        else:
            return -1

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if (len(self.queue) >= 1):
            return False
        else:
            return True

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if (len(self.queue) == self.maxlen):
            return True
        else:
            return False


# Your MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(8)
param_1 = obj.enQueue(3)
param_1 = obj.enQueue(9)
param_1 = obj.enQueue(5)
param_1 = obj.enQueue(0)
param_2 = obj.deQueue()
param_2 = obj.deQueue()
param_5 = obj.isEmpty()
param_5 = obj.isEmpty()
param_4 = obj.Rear()
param_4 = obj.Rear()
param_2 = obj.deQueue()
# param_1 = obj.enQueue(5)
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
