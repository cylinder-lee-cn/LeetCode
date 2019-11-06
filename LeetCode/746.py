"""
746. 使用最小花费爬楼梯

数组的每个索引做为一个阶梯，第 i个阶梯对应着一个非负数的体力花费值 cost[i](索引从0开始)。
每当你爬上一个阶梯你都要花费对应的体力花费值，然后你可以选择继续爬一个阶梯或者爬两个阶梯。
您需要找到达到楼层顶部的最低花费。在开始时，你可以选择从索引为 0 或 1 的元素作为初始阶梯。

示例 1:
输入: cost = [10, 15, 20]
输出: 15
解释: 最低花费是从cost[1]开始，然后走两步即可到阶梯顶，一共花费15。

示例 2:
输入: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
输出: 6
解释: 最低花费方式是从cost[0]开始，逐个经过那些1，跳过cost[3]，一共花费6。

注意：
cost 的长度将会在 [2, 1000]。
每一个 cost[i] 将会是一个Integer类型，范围为 [0, 999]。
"""


class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        all_cast = []
        all_cast.append(cost[0])
        all_cast.append(cost[1])

        for i in range(2, len(cost)):
            all_cast.append(min(all_cast[i - 1], all_cast[i - 2]) + cost[i])

        return min(all_cast[-2:])


s = Solution()
print(s.minCostClimbingStairs([10, 20]))
print(s.minCostClimbingStairs([10, 15, 20]))
print(s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
"""
此题解法：
* 又是一个典型的动态规划的问题。
* 按照官方的提示，每到一个台阶最小的花费就是 cast_at_step= cast[i]+ min(cast[i-1],cast[i-2])
* 循环从2开始（第三步），cast[0]是第一步的花费，cast[1]是第二步，
    每次计算一步就将cast放入List，用于下一次的计算
* 最后就看最后2步哪个是最小的。（都是用前面最小的逐步累加计算出来的）

样例待阅读和理解
        f1 = f2 = 0
        for x in reversed(cost):
            f1, f2 = x + min(f1, f2), f1
        return min(f1, f2)
"""
