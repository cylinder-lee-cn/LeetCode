"""
447. 回旋镖的数量

给定平面上 n 对不同的点，“回旋镖” 是由点表示的元组 (i, j, k) ，
其中 i 和 j 之间的距离和 i 和 k 之间的距离相等（需要考虑元组的顺序）。

找到所有回旋镖的数量。你可以假设 n 最大为 500，所有点的坐标在闭区间 [-10000, 10000] 中。

示例:
输入:
[[0,0],[1,0],[2,0]]
输出:
2

解释:
两个回旋镖为 [[1,0],[0,0],[2,0]] 和 [[1,0],[2,0],[0,0]]
"""


class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        count = 0
        for a in points:
            d = {}
            for b in points:
                dis = (a[0] - b[0])**2 + (a[1] - b[1])**2
                d[dis] = d.get(dis, 0) + 1

            count = count + sum(n * (n - 1) for n in d.values() if n >= 2)

        return count


s = Solution()
print(s.numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]))
"""
此题解法：
* 在座标下有若干点，存在a到b的距离==a到c的距离...，这些点的数量
* 首先遍历所有的点，依次计算相对的距离，使用x^2+y^2不用开方，节省计算量
* 将“距离”：点的数量，存入字典，这样value>=2的就是回旋镖
* 有多少个回旋镖，其实就是给定一个点，然后在相同距离的点n里任取2个，是排列（与顺序有关）P(n,2)
  n!/(n-2)! = n*(n-1)
* 最后将所有结果sum即可
"""
