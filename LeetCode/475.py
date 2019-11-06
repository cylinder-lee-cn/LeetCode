"""
475. 供暖器

冬季已经来临。 你的任务是设计一个有固定加热半径的供暖器向所有房屋供暖。
现在，给出位于一条水平线上的房屋和供暖器的位置，找到可以覆盖所有房屋的最小加热半径。
所以，你的输入将会是房屋和供暖器的位置。你将输出供暖器的最小加热半径。

说明:
给出的房屋和供暖器的数目是非负数且不会超过 25000。
给出的房屋和供暖器的位置均是非负数且不会超过10^9。
只要房屋位于供暖器的半径内(包括在边缘上)，它就可以得到供暖。
所有供暖器都遵循你的半径标准，加热的半径也一样。

示例 1:
输入: [1,2,3],[2]
输出: 1
解释: 仅在位置2上有一个供暖器。如果我们将加热半径设为1，那么所有房屋就都能得到供暖。

示例 2:
输入: [1,2,3,4],[1,4]
输出: 1
解释: 在位置1, 4上有两个供暖器。我们需要将加热半径设为1，这样所有房屋就都能得到供暖。
"""
import bisect


class Solution:
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        list.sort(heaters)
        res, disLeft, disRight = 0, 0, 0
        for house in houses:
            index = bisect.bisect_left(heaters, house)
            disLeft = house - heaters[index - 1] if index - 1 >= 0 else float(
                'inf')
            disRight = heaters[index] - house if index < len(
                heaters) else float('inf')
            res = max(res, min(disLeft, disRight))
        return res


s = Solution()
print(s.findRadius([1, 2, 3], [2]))
print(s.findRadius([1, 2, 3, 4], [1, 4]))
print(s.findRadius([1, 5], [2]))
print(s.findRadius([1, 2, 3, 5, 15], [2, 30]))
"""
此题解法：
* 此题描述有很大的歧义。
* 房子的序列其实是从1开始增量为1的序列，1 2 3 4 5 ... 在这个座标上随机出现房子和加热器。
* 依据以上这个条件来计算加热器的最小加热半径
* 遍历房子，找到每个房子在加热器中的位置（排序好的加热器）算出距离该房子最近的左右两端加热器离房子的距离并取最小值。
最后取出这些最小值中的最大值。边界加判断条件。
* Python:bisect.bisect_left:若找到待查元素，返回元素索引;若没找到待查元素，返回该元素应该存在的位置的索引。
"""
