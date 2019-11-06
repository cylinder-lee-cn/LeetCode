"""
869. 重新排序得到 2 的幂

从正整数 N 开始，我们按任何顺序（包括原始顺序）将数字重新排序，注意其前导数字不能为零。
如果我们可以通过上述方式得到 2 的幂，返回 true；否则，返回 false。

示例 1：
输入：1
输出：true

示例 2：
输入：10
输出：false

示例 3：
输入：16
输出：true

示例 4：
输入：24
输出：false

示例 5：
输入：46
输出：true

提示：
1 <= N <= 10^9
"""


class Solution:
    def reorderedPowerOf2(self, N):
        """
        :type N: int
        :rtype: bool
        """
        nd = {
            '0124', '23334455', '112234778', '125', '23678', '35566',
            '0368888', '128', '4', '0122579', '2', '1289', '011237',
            '01466788', '012356789', '13468', '16', '224588', '23', '0469',
            '234455668', '0248', '0145678', '8', '1', '11266777', '122446',
            '0134449', '256', '46'
        }

        ns = ''.join(sorted(str(N)))
        if ns in nd:
            return True
        else:
            return False


s = Solution()
print(s.reorderedPowerOf2(1))
print(s.reorderedPowerOf2(10))
print(s.reorderedPowerOf2(16))
print(s.reorderedPowerOf2(24))
print(s.reorderedPowerOf2(46))

"""
此题解法：
* 使用了一个取巧的办法，由于题目 条件是 1 <= N <= 10^9，
所以找出所有小于 10^9 的2的幂，然后将结果转换成字符串并排序，放入set中
* 将N转成字符串并排序后，在set中查找，返回是否在set中即可
"""
