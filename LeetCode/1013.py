"""
1013. 将数组分成和相等的三个部分

给定一个整数数组 A，只有我们可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。

形式上，如果我们可以找出索引 i+1 < j
且满足
(A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ...
+ A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。

示例 1：
输出：[0,2,1,-6,6,-7,9,1,2,0,1]
输出：true
解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1

示例 2：
输入：[0,2,1,-6,6,7,9,-1,2,0,1]
输出：false

示例 3：
输入：[3,3,6,5,-2,2,5,1,-9,4]
输出：true
解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

提示：
3 <= A.length <= 50000
-10000 <= A[i] <= 10000
"""


class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        s, y = divmod(sum(A), 3)

        if y > 0:
            return False

        sum_r, sum_l = 0, 0

        ridx, lidx = 0, len(A) - 1
        while ridx < lidx:
            if sum_l != s:
                sum_l = sum_l + A[ridx]
                ridx = ridx + 1

            if sum_r != s:
                sum_r = sum_r + A[lidx]
                lidx = lidx - 1

            if sum_l == s and sum_r == s:
                return True
        return False


s = Solution()
# print(s.canThreePartsEqualSum([0, 2, 1, -6, 6, -7, 9, 1, 2, 0, 1]))
# print(s.canThreePartsEqualSum([0, 2, 1, -6, 6, 7, 9, -1, 2, 0, 1]))
# print(s.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))
print(s.canThreePartsEqualSum([3, 3, 6, 5, -2, 2, 5, 1, -9, 4]))

"""
此题解法：
* 采用双指针
* 先计算出A的合计，然后用3整除来判断，如果无法被3整除，就直接返回False
* 用双指针从两头进行遍历与合计，双指针不能交叉
* 如果从两端都能计算出合计等于 A/3 ，那么就满足条件，反之错误
"""
