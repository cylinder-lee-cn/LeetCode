"""
1010. 总持续时间可被 60 整除的歌曲

在歌曲列表中，第 i 首歌曲的持续时间为 time[i] 秒。

返回其总持续时间（以秒为单位）可被 60 整除的歌曲对的数量。形式上，
我们希望索引的数字  i < j 且有 (time[i] + time[j]) % 60 == 0。

示例 1：

输入：[30,20,150,100,40]
输出：3
解释：这三对的总持续时间可被 60 整数：
(time[0] = 30, time[2] = 150): 总持续时间 180
(time[1] = 20, time[3] = 100): 总持续时间 120
(time[1] = 20, time[4] = 40): 总持续时间 60
示例 2：

输入：[60,60,60]
输出：3
解释：所有三对的总持续时间都是 120，可以被 60 整数。

提示：

1 <= time.length <= 60000
1 <= time[i] <= 500
"""


class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        from collections import defaultdict

        count = 0

        yDict = defaultdict(int)

        for t in time:
            y = t % 60
            ry = 0 if y == 0 else 60 - y

            count = count + yDict[y]
            yDict[ry] = yDict[ry] + 1

        return count


s = Solution()
print(s.numPairsDivisibleBy60([30, 20, 150, 100, 40]))
print(s.numPairsDivisibleBy60([60, 60, 60]))
"""
此题解法：
* 如果A+B能被60整除，那么势必满足 A%60=60-B%60
* 如果其中一个余数为0，那么另外一个的余数也必定为0
* 遍历time，如果一个t%60能在字典中找到对应的记录，就在count上累加计数
* 如果找不到，就将ry计入字典中，并且字典对应计数+1
"""
