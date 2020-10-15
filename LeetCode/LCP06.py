"""
桌上有 n 堆力扣币，每堆的数量保存在数组 coins 中。我们每次可以选择任意一堆，
拿走其中的一枚或者两枚，求拿完所有力扣币的最少次数。

示例 1：
输入：[4,2,1]
输出：4

解释：第一堆力扣币最少需要拿2次，第二堆最少需要拿1次，第三堆最少需要拿 1 次，总共4次即可拿完。

示例 2：
输入：[2,3,10]
输出：8

限制：
1 <= n <= 4
1 <= coins[i] <= 10
"""

from typing import List


class Solution:
    def minCount(self, coins: List[int]) -> int:
        return sum((coin + 1) // 2 for coin in coins)


"""
此题解法：
就是看coins数组中，每一对硬币包含多少个2，可以直接利用每一堆的硬币数量用2整除的商，由于如果
有余数那么商还要增加1（因为要拿完硬币），所以可以用每一堆硬币数量+1来整除2
"""

s = Solution()
print(s.minCount([4, 2, 1]))
print(s.minCount([2, 3, 10]))
