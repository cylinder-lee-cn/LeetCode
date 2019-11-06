"""
981. 基于时间的键值存储

创建一个基于时间的键值存储类 TimeMap，它支持下面两个操作：

1. set(string key, string value, int timestamp)

存储键 key、值 value，以及给定的时间戳 timestamp。
2. get(string key, int timestamp)

返回先前调用 set(key, value, timestamp_prev) 所存储的值，其中 timestamp_prev <= timestamp。
如果有多个这样的值，则返回对应最大的  timestamp_prev 的那个值。
如果没有值，则返回空字符串（""）。

示例 1：

输入：inputs = ["TimeMap","set","get","get","set","get","get"],
inputs = [[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],
          ["foo",4],["foo",5]]
输出：[null,null,"bar","bar",null,"bar2","bar2"]
解释：
TimeMap kv;
kv.set("foo", "bar", 1); // 存储键 "foo" 和值 "bar" 以及时间戳 timestamp = 1
kv.get("foo", 1);  // 输出 "bar"
kv.get("foo", 3); // 输出 "bar" 因为在时间戳 3 和时间戳 2 处没有对应 "foo" 的值，
所以唯一的值位于时间戳 1 处（即 "bar"）
kv.set("foo", "bar2", 4);
kv.get("foo", 4); // 输出 "bar2"
kv.get("foo", 5); // 输出 "bar2"

示例 2：

输入：inputs = ["TimeMap","set","set","get","get","get","get","get"],
inputs = [[],["love","high",10],["love","low",20],["love",5],["love",10],
          ["love",15],["love",20],["love",25]]
输出：[null,null,null,"","high","high","low","low"]

提示：

所有的键/值字符串都是小写的。
所有的键/值字符串长度都在 [1, 100] 范围内。
所有 TimeMap.set 操作中的时间戳 timestamps 都是严格递增的。
1 <= timestamp <= 10^7
TimeMap.set 和 TimeMap.get 函数在每个测试用例中将（组合）调用总计 120000 次。
"""

import collections
import bisect


class TimeMap(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tmdb = collections.defaultdict(list)

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        self.tmdb[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        tmp = self.tmdb.get(key, None)
        if tmp is None:
            return ''

        idx = bisect.bisect(tmp, (timestamp, chr(127)))

        return tmp[idx - 1][-1] if idx > 0 else ''


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set('foo', 'bar', 1)
# obj.get('foo', 1)
# obj.get('foo', 3)
# obj.set('foo', 'bar2', 4)
# obj.get('foo', 4)
# obj.get('foo', 5)
t = TimeMap()
t.set('love', 'high', 10)
t.set('love', 'low', 20)
print(t.get('love', 5))
print(t.get('love', 10))
print(t.get('love', 15))
print(t.get('love', 20))
print(t.get('love', 25))

"""
此题解法：
* 首先利用一下collections中的defaultdict来存放key和一个List，列表中是(timestamp,value)元组
* 由于timestamp是递增的，所以List中的元组也是按照timestamp递增的
* 如果dict中有对应的key值，利用自带的二分法查找(bisect.bisect)
* bisect.bisect(a, x,lo=0, hi=len(a))
* 二分法查找有个技巧，由于value都是小写字母，最大的ascii值是'z'=122，而bisect方法返回在有序列表中插入x的位置索引
  所以将待查找的元组调整为(timestamp,chr(127)),其实可以不是127，只要比122大即可。这样就聚焦为在timestamp上
"""
