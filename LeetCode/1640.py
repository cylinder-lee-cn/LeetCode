"""
1640. 能否连接形成数组
给你一个整数数组 arr ，数组中的每个整数 互不相同 。另有一个由整数数组构成的数组 pieces，
其中的整数也 互不相同 。请你以 任意顺序 连接 pieces 中的数组以形成 arr 。
但是，不允许 对每个数组 pieces[i] 中的整数重新排序。

如果可以连接 pieces 中的数组形成 arr ，返回 true ；否则，返回 false 。

示例 1：
输入：arr = [85], pieces = [[85]]
输出：true

示例 2：
输入：arr = [15,88], pieces = [[88],[15]]
输出：true
解释：依次连接 [15] 和 [88]

示例 3：
输入：arr = [49,18,16], pieces = [[16,18,49]]
输出：false
解释：即便数字相符，也不能重新排列 pieces[0]

示例 4：
输入：arr = [91,4,64,78], pieces = [[78],[4,64],[91]]
输出：true
解释：依次连接 [91]、[4,64] 和 [78]

示例 5：
输入：arr = [1,3,5,7], pieces = [[2,4,6,8]]
输出：false

提示：
1 <= pieces.length <= arr.length <= 100
sum(pieces[i].length) == arr.length
1 <= pieces[i].length <= arr.length
1 <= arr[i], pieces[i][j] <= 100
arr 中的整数 互不相同
pieces 中的整数 互不相同（也就是说，如果将 pieces 扁平化成一维数组，数组中的所有整数互不相同）
"""

from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        arr_dict = {}
        for idx, v in enumerate(arr):
            arr_dict[v] = idx
        # print(arr_dict)

        for p in pieces:
            if p[0] not in arr_dict or p[-1] not in arr_dict:
                return False
            elif p != arr[arr_dict[p[0]]:arr_dict[p[-1]]+1]:
                return False
        return True


s = Solution()
print(s.canFormArray([85], [[85]]))
print(s.canFormArray([15, 88], [[88], [15]]))
print(s.canFormArray([49, 18, 16], [[16, 18, 49]]))
print(s.canFormArray([91, 4, 64, 78], [[78], [4, 64], [91]]))
print(s.canFormArray([1, 3, 5, 7],  [[2, 4, 6, 8]]))
print(s.canFormArray([100, 2, 98, 28, 44, 55, 37],
                     [[28, 46, 57], [37, 19, 40, 38]]))

"""
此题解法：
* 先将arr的list遍历，将元素和对应的索引放入字典中
* 然后遍历pieces的每个元素：p（元素是list）
* 如果p[0]不在字典中就返回false
* 如果p[0]在字典中就继续判断整个p，那p[0]在arr_dict中的idx以及p[-1]在arr_dict的索引，
  对应在arr中的子串是否与p相同，如果不相同，就返回false
* 如上判断如果均不返回false，就返回true
"""
