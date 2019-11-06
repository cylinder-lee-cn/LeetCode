"""
1128. 等价多米诺骨牌对的数量

给你一个由一些多米诺骨牌组成的列表 dominoes。

如果其中某一张多米诺骨牌可以通过旋转 0 度或 180 度得到另一张多米诺骨牌，我们就认为这两张牌是等价的。

形式上，dominoes[i] = [a, b] 和 dominoes[j] = [c, d] 
等价的前提是 a==c 且 b==d，或是 a==d 且 b==c。

在 0 <= i < j < dominoes.length 的前提下，
找出满足 dominoes[i] 和 dominoes[j] 等价的骨牌对 (i, j) 的数量。

示例：

输入：dominoes = [[1,2],[2,1],[3,4],[5,6]]
输出：1

提示：
1 <= dominoes.length <= 40000
1 <= dominoes[i][j] <= 9
"""


class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """

        dCount = {}
        result = 0

        for a in dominoes:
            x = min(a)
            y = max(a)
            dCount[(x, y)] = dCount.get((x, y), 0) + 1

        for i in dCount.values():
            result = result + i * (i - 1)

        return result >> 1


s = Solution()
print(s.numEquivDominoPairs([[1, 2], [2, 1], [2, 1], [3, 4], [5, 6]]))
"""
此题解法：
* 如果两个数组一样，那就说明数组排序后完全一致。
* 使用字典来统计相同数组的个数。
* 将每个子数组（骨牌）排序，然后转换成元组，在字典中计数
* 遍历字典的values()
* value==1 说明没有相同的骨牌，value==2说明有1对，value==3说明有3对（两两取），value==4说明有6对
* 就是Cnr组合，所以是i*(i-1)/2,可以最后合计再除2
"""
