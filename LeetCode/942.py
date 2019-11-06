"""
942. 增减字符串匹配

给定只含 "I"（增大）或 "D"（减小）的字符串 S ，令 N = S.length。

返回 [0, 1, ..., N] 的任意排列 A 使得对于所有 i = 0, ..., N-1，都有：

如果 S[i] == "I"，那么 A[i] < A[i+1]
如果 S[i] == "D"，那么 A[i] > A[i+1]

示例 1：
输出："IDID"
输出：[0,4,1,3,2]

示例 2：
输出："III"
输出：[0,1,2,3]

示例 3：
输出："DDI"
输出：[3,2,0,1]

提示：
1 <= S.length <= 1000
S 只包含字符 "I" 或 "D"。
"""


class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        minv = 0
        maxv = len(S)
        result = []

        for s in S:
            if (s == 'I'):
                result.append(minv)
                minv = minv + 1
            elif (s == 'D'):
                result.append(maxv)
                maxv = maxv - 1
        result.append(maxv)
        return result


s = Solution()
print(s.diStringMatch('IDID'))
"""
此题解法：
* 每次I的前一个位置都是从最小值开始往上加一得到的,
* 每次D的前一个位置都是从最大值开始往下减一得到的,
* 最后minv和maxv将相同，并且这个补充到result中
"""
