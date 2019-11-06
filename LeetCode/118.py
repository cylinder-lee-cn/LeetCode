"""
118. 杨辉三角
给定一个非负整数 numRows，生成杨辉三角的前 numRows 行。

在杨辉三角中，每个数是它左上方和右上方的数的和。

示例:
输入: 5
输出:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if (numRows <= 0):
            return []

        nums = []
        for i in range(numRows):
            tmp = []
            for j in range(i + 1):
                if (j == 0 or j == i):
                    tmp.append(1)
                else:
                    tmp.append(nums[i - 1][j - 1] + nums[i - 1][j])
            nums.append(tmp)
            print(tmp)

        return nums


s = Solution()
print(s.generate(6))
