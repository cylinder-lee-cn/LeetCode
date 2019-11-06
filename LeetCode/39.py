"""
39. 组合总和

给定一个无重复元素的数组 candidates 和一个目标数 target ，
找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：
所有数字（包括 target）都是正整数。
解集不能包含重复的组合。

示例 1:
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]

示例 2:
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candset = set(candidates)
        result = set()
        hasOne = bool(1 in candset)

        for c in candidates:
            i = 0
            t = target
            run = True
            while run:
                t = t - c
                i = i + 1
                if t > 0 and t in candset:
                    tmp = [c] * i
                    tmp.append(t)
                elif t > 0 and t not in candset:
                    continue
                elif t == 0:
                    tmp = [c] * i
                elif t < 0:
                    run = False
                print(tmp)


s = Solution()
s.combinationSum([2, 3, 6, 7], 7)
s.combinationSum([1, 2, 3, 5], 8)
