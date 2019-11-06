"""
703. 数据流中的第K大元素

设计一个找到数据流中第K大元素的类（class）。注意是排序后的第K大元素，不是第K个不同的元素。

你的 KthLargest 类需要一个同时接收整数 k 和整数数组nums 的构造器，
它包含数据流中的初始元素。每次调用 KthLargest.add，返回当前数据流中第K大的元素。

示例:
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
初始化以后是[2，4，5，8]
kthLargest.add(3);   // returns 4
加了一个3后[2，3，4，5，8] 所以第三大的是4
kthLargest.add(5);   // returns 5
加个5后[2，3，4，5，5，8] 所以第三大是5
kthLargest.add(10);  // returns 5
加一个10后[2，3，4，5，5，8，10] 第三大还是5
kthLargest.add(9);   // returns 8
加一个9后[2，3，4，5，5，8，9，10]第三大是8
kthLargest.add(4);   // returns 8
加一个4后[2，4，4，5，5，8，9，10]第三大是8

说明:
你可以假设 nums 的长度≥ k-1 且k ≥ 1。
"""
import heapq


class KthLargest(object):
    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.pool = nums
        self.size = len(self.pool)
        self.k = k
        heapq.heapify(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if self.size < self.k:
            heapq.heappush(self.pool, val)
            self.size += 1
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


# Your KthLargest object will be instantiated and called as such:

obj = KthLargest(3, [1, 1])
print(obj.add(1))
print(obj.add(1))
print(obj.add(3))
print(obj.add(3))
print(obj.add(3))
print(obj.add(4))
print(obj.add(4))
print(obj.add(4))
"""
此题解法：
* 网络上给出的方案是使用‘最小堆’，维护一个长度是k的最小堆，需要引入heapq的库。
* 每次add的时候需要判断一下最小堆的长度
"""
