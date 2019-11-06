"""
1018. 可被 5 整除的二进制前缀

给定由若干 0 和 1 组成的数组 A。
我们定义 N_i：从 A[0] 到 A[i] 的第 i 个子数组被解释为一个二进制数（从最高有效位到最低有效位）。

返回布尔值列表 answer，只有当 N_i 可以被 5 整除时，答案 answer[i] 为 true，否则为 false。

示例 1：
输入：[0,1,1]
输出：[true,false,false]
解释：
输入数字为 0, 01, 011；也就是十进制中的 0, 1, 3 。只有第一个数可以被 5 整除，因此 answer[0] 为真。

示例 2：
输入：[1,1,1]
输出：[false,false,false]

示例 3：
输入：[0,1,1,1,1,1]
输出：[true,false,false,false,true,false]

示例 4：
输入：[1,1,1,0,1]
输出：[false,false,false,false,false]

提示：
1 <= A.length <= 30000
A[i] 为 0 或 1
"""


class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        startNum = 0
        result = []
        for a in A:
            startNum = ((startNum << 1) + a) % 5
            if startNum == 0:
                result.append(True)
            else:
                result.append(False)
        return result


s = Solution()
print(s.prefixesDivBy5([0, 1, 1]))
print(s.prefixesDivBy5([1, 1, 1]))
print(s.prefixesDivBy5([0, 1, 1, 1, 1, 1]))
print(s.prefixesDivBy5([1, 1, 1, 0, 1]))

"""
此题解法：
* 顺序读取数组，来计算对应的数值，然后在用5判断是否能够整除
* 默认最高位是0，计算方法是 最高位×2+当前位。
* 如[0,1,1]，依次计算就是:
  0 -> 0*2+0 同时将最高位变更为当前计算值:0
  1 -> 0*2+1 同时将最高位变更为当前计算值:1
  1 -> 1*2+1 同时将最高位变更为当前计算值:3
* 这样只需要遍历一次数组。
* 为了提高效率，每次只需要使用计算值后整除5的余数，作为下次计算的最高位
  1 -> 0*2+1 同时将最高位变更为当前计算值:1%5=1
  1 -> 1*2+1 同时将最高位变更为当前计算值:3%5=3
  1 -> 3*2+1 同时将最高位变更为当前计算值:7%5=2
  x -> 2*2+x ....        
"""
