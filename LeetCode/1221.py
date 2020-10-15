"""
在一个「平衡字符串」中，'L' 和 'R' 字符的数量是相同的。
给出一个平衡字符串 s，请你将它分割成尽可能多的平衡字符串。
返回可以通过分割得到的平衡字符串的最大数量。

示例 1：
输入：s = "RLRRLLRLRL"
输出：4
解释：s 可以分割为 "RL", "RRLL", "RL", "RL", 每个子字符串中都包含相同数量的 'L' 和 'R'。

示例 2：
输入：s = "RLLLLRRRLR"
输出：3
解释：s 可以分割为 "RL", "LLLRRR", "LR", 每个子字符串中都包含相同数量的 'L' 和 'R'。

示例 3：
输入：s = "LLLLRRRR"
输出：1
解释：s 只能保持原样 "LLLLRRRR".

提示：
1 <= s.length <= 1000
s[i] = 'L' 或 'R'
分割得到的每个字符串都必须是平衡字符串。
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count, result = 0, 0
        for c in s:
            if c == 'L':
                count = count+1
            else:
                count = count-1
            if count == 0:
                result = result+1
        return result


s = Solution()
print(s.balancedStringSplit('RLRRLLRLRL'))
print(s.balancedStringSplit('RLLLLRRRLR'))
print(s.balancedStringSplit('LLLLRRRR'))
print(s.balancedStringSplit('RRLRRLRLLLRL'))

"""
此题解法：
* 类似括号匹配的问题，L相当与左括号，R相当于右括号；
* 左括号入栈，遇到右括号出栈，如果栈空那么就属于一次完整的匹配
* RRLRRLRLLLRL 分割成 RRLRRLRLLL 和 RL 两个子串
* R或L不要求连续，只要求数量相同
"""
