"""
933. 最近的请求次数

写一个 RecentCounter 类来计算最近的请求。
它只有一个方法：ping(int t)，其中 t 代表以毫秒为单位的某个时间。
返回从 3000 毫秒前到现在的 ping 数。
任何处于 [t - 3000, t] 时间范围之内的 ping 都将会被计算在内，包括当前（指 t 时刻）的 ping。
保证每次对 ping 的调用都使用比之前更大的 t 值。

示例：
输入：inputs = ["RecentCounter","ping","ping","ping","ping"],
inputs = [[],[1],[100],[3001],[3002]]
输出：[null,1,2,3,3]

提示：
每个测试用例最多调用 10000 次 ping。
每个测试用例会使用严格递增的 t 值来调用 ping。
每次调用 ping 都有 1 <= t <= 10^9。
"""


class RecentCounter:
    def __init__(self):
        self.pings = []
        self.pl = 0
        self.idx = 0

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        self.pings.append(t)
        self.pl = self.pl + 1
        while 1:
            if (self.pings[self.idx] >= (t - 3000)):
                return self.pl - self.idx
            else:
                self.idx = self.idx + 1


# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
print(obj.ping(1))
print(obj.ping(100))
print(obj.ping(3001))
print(obj.ping(3002))

"""
此题解法：
* 不能使用将ping值放入一个List中，然后按照下限统计的方式，这样效率太低，因为要多次遍历这个List。
* 使用一个固定的指针的来存放List的索引。
* 在使用一个pl来存放List的长度，每次将t加入List中，将pl递增1，省得用len来计算，节省时间
* 因为是3000以内的都算上，所以List中存放t，只要List中 >= t-3000 都是需要的ping个数。
  而且t永远是递增的，所以一旦找到一个符合条件的index，下一次就只从这个index来比较就可以。
* 如果不符合条件就将index递增1，比较下一个。这样时间复杂度肯定是O(n)
"""
