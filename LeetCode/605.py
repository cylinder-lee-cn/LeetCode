"""
605. 种花问题

假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。
可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。
能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True

示例 2:
输入: flowerbed = [1,0,0,0,1], n = 2
输出: False

注意:
数组内已种好的花不会违反种植规则。
输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。

"""


class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        count = []
        i = 0
        f_len = len(flowerbed)
        for k, f in enumerate(flowerbed):
            if (f == 0):
                if (k == 0):
                    i = i + 1
                if (k == f_len - 1):
                    i = i + 1
                i = i + 1
            else:
                count.append(i)
                i = 0
        count.append(i)
        return sum([(x - 1) // 2 for x in count if (x > 2)]) >= n


s = Solution()
# print(s.canPlaceFlowers([1, 0, 0, 0, 1, 0, 0, 0, 1], 3))
print(s.canPlaceFlowers([0, 0, 0], 1))

"""
此题解法：
* 种花有间隔，也就是说最标准的情况是 0，1，0。 1的两边是0
* 特殊情况，[，1，0 或者是 0，1，] ，正好是两端的地方。
* 标准情况下可得连续0的数量-1 再除以2 取商就是可以种花的数量 count(0)-1 // 2
* 统计0的时候，如果正好是起点和终点需要多增加1
* 分别计算 count(0)-1 //2 汇总后和n比较即可
"""
