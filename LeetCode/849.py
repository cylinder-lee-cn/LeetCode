"""
849. 到最近的人的最大距离

在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。
至少有一个空座位，且至少有一人坐在座位上。
亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
返回他到离他最近的人的最大距离。

示例 1：
输入：[1,0,0,0,1,0,1]
输出：2
解释：
如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
因此，他到离他最近的人的最大距离是 2 。

示例 2：
输入：[1,0,0,0]
输出：3
解释：
如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
这是可能的最大距离，所以答案是 3 。
提示：

1 <= seats.length <= 20000
seats 中只含有 0 和 1，至少有一个 0，且至少有一个 1。
"""


class Solution:
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        idx = [0]
        idx.extend([i for i, v in enumerate(seats) if v == 1])
        idx.append(len(seats) - 1)
        position = [(a - b) // 2 for a, b in zip(idx[1:], idx)]
        position.append(idx[1] - idx[0])
        position.append(idx[-1] - idx[-2])
        return max(position)


s = Solution()
print(s.maxDistToClosest([1, 0, 0, 0, 1, 0, 1]))
print(s.maxDistToClosest([1, 0, 0, 0]))
print(s.maxDistToClosest([0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0]))
"""
此题解法：
* 找到所有1的索引，根据1的索引就能计算alex的位置和距离1的距离
* [1,0,0,0,1,0,1]获取1的index是[0,4,6],前后补上0和len(seats)，[0,0,4,6,6]
* 两两计算差值整除2，头尾特殊处理，头（0，0），尾（6，6）
* 如果坐在头尾alex的距离就是两个索引直接相减
* (0-0),(0-0)//2,(4-2)//2,(6-4)//2,(6-6)
* [0,0,2,1,0],max就是2
* 如果seats是[1,0,0,0]，1的索引位置加上头尾是[0,0,3],计算后是[0,0,1,3]，max是3
"""
