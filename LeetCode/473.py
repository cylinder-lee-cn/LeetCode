"""
473. 火柴拼正方形


还记得童话《卖火柴的小女孩》吗？现在，你知道小女孩有多少根火柴，请找出一种能使用所有火柴拼成一个正方形的方法。
不能折断火柴，可以把火柴连接起来，并且每根火柴都要用到。

输入为小女孩拥有火柴的数目，每根火柴用其长度表示。输出即为是否能用所有的火柴拼成正方形。

示例 1:
输入: [1,1,2,2,2]
输出: true

解释: 能拼成一个边长为2的正方形，每边两根火柴。

示例 2:
输入: [3,3,3,3,4]
输出: false

解释: 不能用所有火柴拼成一个正方形。

注意:
给定的火柴长度和在 0 到 10^9之间。
火柴数组的长度不超过15。
"""


class Solution:
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nl = len(nums)

        if nl <= 3:
            return False

        nums.sort(reverse=True)
        sl, lm = divmod(sum(nums), 4)

        if lm > 0:
            return False
        if nums[0] > sl or nums[-1] < 0:
            return False

        result = [0] * 4

        def dfs(ns, res, pos, target):
            if pos > nl - 1:
                return all(x == target for x in res)
            for i in range(4):
                if res[i] + ns[pos] > target:
                    continue
                else:
                    res[i] = res[i] + ns[pos]
                if (dfs(ns, res, pos + 1, target)):
                    return True
                res[i] = res[i] - ns[pos]
            return False
        return dfs(nums, result, 0, sl)


s = Solution()
print(s.makesquare([1, 1, 2, 2, 2]))
print(s.makesquare([3, 3, 3, 3, 4]))
print(s.makesquare([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3]))
