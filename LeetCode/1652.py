"""
1652. 拆炸弹
你有一个炸弹需要拆除，时间紧迫！你的情报员会给你一个长度为n的循环数组 code 以及一个密钥 k。

为了获得正确的密码，你需要替换掉每一个数字。所有数字会 同时 被替换。

如果 k > 0 ，将第 i 个数字用 接下来 k 个数字之和替换。
如果 k < 0 ，将第 i 个数字用 之前 k 个数字之和替换。
如果 k == 0 ，将第 i 个数字用 0 替换。
由于 code 是循环的，code[n-1] 下一个元素是 code[0]，且 code[0] 前一个元素是 code[n-1]。

给你 循环 数组 code 和整数密钥 k ，请你返回解密后的结果来拆除炸弹！

示例 1：
输入：code = [5,7,1,4], k = 3
输出：[12,10,16,13]
解释：每个数字都被接下来 3 个数字之和替换。解密后的密码为 [7+1+4, 1+4+5, 4+5+7, 5+7+1]。
注意到数组是循环连接的。

示例 2：
输入：code = [1,2,3,4], k = 0
输出：[0,0,0,0]
解释：当 k 为 0 时，所有数字都被 0 替换。

示例 3：
输入：code = [2,4,9,3], k = -2
输出：[12,5,6,13]
解释：解密后的密码为[3+9, 2+3, 4+2, 9+4]。注意到数组是循环连接的。如果k是负数，
那么和为之前的数字。

提示：
n == code.length
1 <= n <= 100
1 <= code[i] <= 100
-(n - 1) <= k <= n - 1
"""

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        code_len = len(code)
        code_sum = sum(code)
        result = [0]*code_len

        if k == 0:
            return result

        if abs(k) == code_len-1:
            return [code_sum-x for x in code]

        if k == 1:
            tmp = code.pop(0)
            code.append(tmp)
            return code

        if k == -1:
            tmp = code.pop()
            code.insert(0, tmp)
            return code

        if k > 1:
            for i in range(code_len):
                for j in range(k):
                    result[i] = result[i] + code[(i+1+j) % code_len]
            return result

        if k < -1:
            for i in range(code_len):
                for j in range(-k):
                    result[i] = result[i]+code[(i-1-j+code_len) % code_len]
            return result


s = Solution()
print(s.decrypt([5, 7, 1, 4], 1))
print(s.decrypt([5, 7, 1, 4], -1))
print(s.decrypt([2, 4, 9, 3], 2))
print(s.decrypt([2, 4, 9, 3], -2))

"""
此题解法：
* 将特殊情况都分类了，k==0时，abs(k)==length-1时，还有k==1 k==-1时
* 然后是通用情况 1<k<length-1
* 由于是循环数组，所以要利用索引的递增以及数组长度取余来实现循环，比如数组长度是4，当索引指针
指向0 1 2 3 时数组正常访问，当继续增加时 4 5 6 7 其实就是数组循环，通过取余 4%4 5%4 
6%4 7%4 实现索引的重复
"""
