"""
908. 最小差值 I

给定一个整数数组 A，对于每个整数 A[i]，我们可以选择任意 x 满足 -K <= x <= K，
而且将 A[i]= x +A[i] 中。在此过程之后，我们得到一些数组 B。

返回 B 的最大值和 B 的最小值之间可能存在的最小差值。

示例 1：
输入：A = [1], K = 0
输出：0
解释：B = [1]

示例 2：
输入：A = [0,10], K = 2
输出：6
解释：B = [2,8]

示例 3：
输入：A = [1,3,6], K = 3
输出：0
解释：B = [3,3,3] 或 B = [4,4,4]

提示：
1 <= A.length <= 10000
0 <= A[i] <= 10000
0 <= K <= 10000
"""


class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        K = K * 2

        min_a = min(A)
        max_a = max(A)

        max_diff = max_a - min_a

        if (max_diff <= K):
            return 0
        else:
            return max_diff - K


s = Solution()
print(s.smallestRangeI([1], 0))
print(s.smallestRangeI([0, 10], 2))
print(s.smallestRangeI([1, 3, 6], 3))

"""
此题解法：
* K的取值是 [-K,+K]，也就是值的最大浮动范围是K×2
* A中的最小值和最大值加[-K，+K]后依旧是B的最小值和最大值
* 如果max(A)-min(A) <=2K ，说明能通过选择K将所有的值都变相同，那么最小的差值一定是0
* 如果>2K ，那么只能将差值缩小2K，就是max(A)-min(A)-2K

"""
