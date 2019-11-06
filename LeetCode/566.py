"""
566. 重塑矩阵

在MATLAB中，有一个非常有用的函数 reshape，它可以将一个矩阵重塑为另一个大小不同的新矩阵，但保留其原始数据。
给出一个由二维数组表示的矩阵，以及两个正整数r和c，分别表示想要的重构的矩阵的行数和列数。
重构后的矩阵需要将原始矩阵的所有元素以相同的行遍历顺序填充。
如果具有给定参数的reshape操作是可行且合理的，则输出新的重塑矩阵；否则，输出原始矩阵。

示例 1:
输入:
nums =
[[1,2],
 [3,4]]
r = 1, c = 4
输出:
[[1,2,3,4]]
解释:
行遍历nums的结果是 [1,2,3,4]。新的矩阵是 1 * 4 矩阵, 用之前的元素值一行一行填充新矩阵。

示例 2:
输入:
nums =
[[1,2],
 [3,4]]
r = 2, c = 4
输出:
[[1,2],
 [3,4]]
解释:
没有办法将 2 * 2 矩阵转化为 2 * 4 矩阵。 所以输出原矩阵。

注意：
给定矩阵的宽和高范围在 [1, 100]。
给定的 r 和 c 都是正数。
"""


class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        o_r = len(nums)
        o_c = len(nums[0])

        if (o_r * o_c != r * c):
            return nums

        # count = 0
        # tmp = []
        # result = []
        # for i, row in enumerate(nums):
        #     for j, v in enumerate(row):
        #         if (count < c):
        #             tmp.append(v)
        #             count = count + 1
        #         else:
        #             result.append(tmp)
        #             tmp = [][:]
        #             tmp.append(v)
        #             count = 1
        # result.append(tmp)
        # return result

        one_line = [n for row in nums for n in row]
        result = [one_line[i:i + c] for i in range(0, r * c, c)]
        return result


s = Solution()
print(s.matrixReshape([[1, 2], [3, 4]], 1, 4))
print(s.matrixReshape([[1, 2], [3, 4]], 4, 1))
print(s.matrixReshape([[1, 2], [3, 4]], 2, 2))


"""
此题解法：
* 首先要判断一下现有数组的长宽相乘是否与r乘c相同，如果不等就返回原始nums

* 解法一，循环nums，按照计数器值为c来取数据，放入List，计数满了以后添加到result中。

解法二，列表生成器，现将原nums转为一维数组。
        然后，将一维数组用列表生成器转制成为所需r乘c的二维数组
"""
