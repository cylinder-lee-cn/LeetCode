"""
641. 设计循环双端队列

设计实现双端队列。
你的实现需要支持以下操作：

MyCircularDeque(k)：构造函数,双端队列的大小为k。
insertFront()：将一个元素添加到双端队列头部。 如果操作成功返回 true。
insertLast()：将一个元素添加到双端队列尾部。如果操作成功返回 true。
deleteFront()：从双端队列头部删除一个元素。 如果操作成功返回 true。
deleteLast()：从双端队列尾部删除一个元素。如果操作成功返回 true。
getFront()：从双端队列头部获得一个元素。如果双端队列为空，返回 -1。
getRear()：获得双端队列的最后一个元素。 如果双端队列为空，返回 -1。
isEmpty()：检查双端队列是否为空。
isFull()：检查双端队列是否满了。

示例：
MyCircularDeque circularDeque = new MycircularDeque(3); // 设置容量大小为3
circularDeque.insertLast(1);			// 返回 true
circularDeque.insertLast(2);			// 返回 true
circularDeque.insertFront(3);			// 返回 true
circularDeque.insertFront(4);			// 已经满了，返回 false
circularDeque.getRear();  				// 返回  2
circularDeque.isFull();				// 返回 true
circularDeque.deleteLast();			// 返回 true
circularDeque.insertFront(4);			// 返回 true
circularDeque.getFront();				// 返回 4

提示：
所有值的范围为 [1, 1000]
操作次数的范围为 [1, 1000]
请不要使用内置的双端队列库。
"""


class MyCircularDeque:
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the deque to be k.
        :type k: int
        """
        self.maxlen = k
        self.dqueue = []

    def insertFront(self, value):
        """
        Adds an item at the front of Deque.
        Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if (self.isFull()):
            return False
        else:
            self.dqueue.insert(0, value)
            return True

    def insertLast(self, value):
        """
        Adds an item at the rear of Deque.
        Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if (self.isFull()):
            return False
        else:
            self.dqueue.append(value)
            return True

    def deleteFront(self):
        """
        Deletes an item from the front of Deque.
        Return true if the operation is successful.
        :rtype: bool
        """
        if (self.isEmpty()):
            return False
        else:
            self.dqueue.pop(0)
            return True

    def deleteLast(self):
        """
        Deletes an item from the rear of Deque.
        Return true if the operation is successful.
        :rtype: bool
        """
        if (self.isEmpty()):
            return False
        else:
            self.dqueue.pop()
            return True

    def getFront(self):
        """
        Get the front item from the deque.
        :rtype: int
        """
        if (self.isEmpty()):
            return -1
        else:
            return self.dqueue[0]

    def getRear(self):
        """
        Get the last item from the deque.
        :rtype: int
        """
        if (self.isEmpty()):
            return -1
        else:
            return self.dqueue[-1]

    def isEmpty(self):
        """
        Checks whether the circular deque is empty or not.
        :rtype: bool
        """
        if (len(self.dqueue) == 0):
            return True
        else:
            return False

    def isFull(self):
        """
        Checks whether the circular deque is full or not.
        :rtype: bool
        """
        if (len(self.dqueue) >= self.maxlen):
            return True
        else:
            return False


# Your MyCircularDeque object will be instantiated and called as such:
s = MyCircularDeque(3)
print(s.insertLast(1))  # 返回 true
print(s.insertLast(2))  # 返回 true
print(s.insertFront(3))  # 返回 true
print(s.insertFront(4))  # 已经满了，返回 false
print(s.getRear())  # 返回  2
print(s.isFull())  # 返回 true
print(s.deleteLast())  # 返回 true
print(s.insertFront(4))  # 返回 true
print(s.getFront())  # 返回 4
