"""
914. 卡牌分组
给定一副牌，每张牌上都写着一个整数。

此时，你需要选定一个数字 X，使我们可以将整副牌按下述规则分成 1 组或更多组：

每组都有 X 张牌。
组内所有的牌上都写着相同的整数。
仅当你可选的 X >= 2 时返回 true。

示例 1：
输入：[1,2,3,4,4,3,2,1]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[3,3]，[4,4]

示例 2：
输入：[1,1,1,2,2,2,3,3]
输出：false
解释：没有满足要求的分组。

示例 3：
输入：[1]
输出：false
解释：没有满足要求的分组。

示例 4：
输入：[1,1]
输出：true
解释：可行的分组是 [1,1]

示例 5：
输入：[1,1,2,2,2,2]
输出：true
解释：可行的分组是 [1,1]，[2,2]，[2,2]

提示：
1 <= deck.length <= 10000
0 <= deck[i] < 10000
"""


class Solution:
    def hasGroupsSizeX(self, deck):
        """
        :type deck: List[int]
        :rtype: bool
        """
        ddict = {}
        for d in deck:
            ddict[d] = ddict.get(d, 0) + 1

        decksum = list(ddict.values())

        minsum = min(decksum)
        print(decksum, minsum)

        for g in range(2, minsum + 1):
            if all(val % g == 0 for val in decksum):
                return True

        return False


s = Solution()
# print(s.hasGroupsSizeX([1, 2, 3, 4, 4, 3, 2, 1]))
# print(s.hasGroupsSizeX([1, 1, 1, 2, 2, 2, 3, 3]))
# print(s.hasGroupsSizeX([1]))
# print(s.hasGroupsSizeX([1, 1]))
# print(s.hasGroupsSizeX([1, 1, 2, 2, 2, 2]))
# print(s.hasGroupsSizeX([1, 1, 1, 1, 1, 1, 2, 2, 2, 2]))
# print(s.hasGroupsSizeX([0, 0, 0, 0, 0, 1, 1, 2, 3, 4]))
print(s.hasGroupsSizeX([0, 0, 0, 1, 1, 1, 2, 2, 2]))
"""
此题解法：
* 统计每个数字以及出现的次数，放入字典
* 将次数作为一个List
解1：
找到这个次数List中的最大公约数，如果公约数>=2那就是True，反之False

from functools import reduce
import collections
class Solution:
    def hasGroupsSizeX(self, deck):
        def gcd(a, b):
            while b: a, b = b, a % b
            return a
        count = collections.Counter(deck).values()
        return reduce(gcd, count) > 1

解2:
从2开始逐步递增，最大到min（List次数），看看是否能将List中所有的数字整除。
如果可以那就是True，反之False

"""
