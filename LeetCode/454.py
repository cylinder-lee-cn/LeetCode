"""
454. 四数相加 II

给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 (i, j, k, l) ，
使得 A[i] + B[j] + C[k] + D[l] = 0。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 ≤ N ≤ 500 。
所有整数的范围在 -228 到 228 - 1 之间，最终结果不会超过 231 - 1 。

例如:
输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""


class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """

        if len(A) == 0:
            return 0

        dict1 = {}
        result = 0

        for a in A:
            for b in B:
                p1 = a + b
                dict1[p1] = dict1.get(p1, 0) + 1

        for c in C:
            for d in D:
                p2 = -(c + d)
                result = result + dict1.get(p2, 0)

        return result


s = Solution()
print(s.fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]))

"""
此题解法：
* 先遍历AB两个list，计算出所有2个元素的和以及出现的次数，存放于dict1字典中
* 再遍历CD两个list，计算所有2个元素的和，然后去dict1中查找对应的负值，如果找到，就累加dict1中的次数
  找不到次数就是0
* 返回累加值，好处是这个题目不用排重
"""

