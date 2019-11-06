"""
705. 设计哈希集合

不使用任何内建的哈希表库设计一个哈希集合

具体地说，你的设计应该包含以下的功能

add(value)：向哈希集合中插入一个值。
contains(value) ：返回哈希集合中是否存在这个值。
remove(value)：将给定值从哈希集合中删除。如果哈希集合中没有这个值，什么也不做。

示例:
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // 返回 true
hashSet.contains(3);    // 返回 false (未找到)
hashSet.add(2);          
hashSet.contains(2);    // 返回 true
hashSet.remove(2);          
hashSet.contains(2);    // 返回  false (已经被删除)

注意：
所有的值都在 [1, 1000000]的范围内。
操作的总数目在[1, 10000]范围内。
不要使用内建的哈希集合库。
"""


class MyHashSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashtable = [0] * 1000001

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.hashtable[key] = 1

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        self.hashtable[key] = 0

    def contains(self, key):
        """
        Returns true if this set did not already contain the specified element
        :type key: int
        :rtype: bool
        """
        return True if self.hashtable[key] == 1 else False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
"""
此题解法（来自网络）：因为值的范围是确定的，那么，可以申请一个长度为1000001的数组，使用下标作为索引，来保存数据。
"""
