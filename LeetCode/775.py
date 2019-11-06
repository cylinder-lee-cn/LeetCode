"""
775. 全局倒置与局部倒置

数组 A 是 [0, 1, ..., N - 1] 的一种排列，N 是数组 A 的长度。
全局倒置指的是 i,j 满足 0 <= i < j < N 并且 A[i] > A[j] ，
局部倒置指的是 i 满足 0 <= i < N 并且 A[i] > A[i+1] 。

当数组 A 中全局倒置的数量等于局部倒置的数量时，返回 true 。

示例 1:
输入: A = [1,0,2]
输出: true
解释: 有 1 个全局倒置，和 1 个局部倒置。

示例 2:
输入: A = [1,2,0]
输出: false
解释: 有 2 个全局倒置，和 1 个局部倒置。

注意:
A 是 [0, 1, ..., A.length - 1] 的一种排列
A 的长度在 [1, 5000]之间
这个问题的时间限制已经减少了。
"""


class Solution:
    def isIdealPermutation(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        for i in range(len(A)):
            if abs(A[i] - i) > 1:
                return False
        return True


s = Solution()
print(s.isIdealPermutation([1, 0, 2]))
print(s.isIdealPermutation([1, 2, 0]))
print(s.isIdealPermutation([2, 1, 0]))
print(s.isIdealPermutation([0, 2, 3, 1]))
"""
此题解法：
* 首先局部倒置也属于全局倒置，也就是说只要出现索引差值>=2的倒置（全局倒置）就说明要返回False
* 第二这个数组是0，1，…… N-1 的连续数字，也就是说如果任意一个数字i，没有出现在i-1，i，i+1这三个索引位上
  就一定会出现一个不是局部倒置的全局倒置
"""
