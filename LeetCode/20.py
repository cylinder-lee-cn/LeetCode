"""
20. 有效的括号
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:
输入: "()"
输出: true

示例 2:
输入: "()[]{}"
输出: true

示例 3:
输入: "(]"
输出: false

示例 4:
输入: "([)]"
输出: false

示例 5:
输入: "{[]}"
输出: true
"""


class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = {'(', '[', '{'}
        right = {')', ']', '}'}

        pair = {')': '(', ']': '[', '}': '{'}

        s = s.replace(' ', '')
        l = len(s)

        stack = []

        if l == 0:
            return True
        if l % 2 > 0:
            return False
        for i in range(l):
            ch = s[i]
            if ch in left:
                stack.append(ch)
            elif ch in right:
                if len(stack) == 0:
                    return False
                if stack[-1] == pair.get(ch):
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False


S = Solution()
print(S.isValid('   (  )}  '))
print(S.isValid('(()()[]{})[])'))

"""
解法源自网上: 利用栈的原理进行最近匹配, 栈:先进后出
* 如果是空字符串返回True
* 删除源字符串中所有的空格
* 如果有效字符数量是奇数,则返回False
* 从字符串的左边第一个字符开始依次判断:
    1. 如果是左括号,放入栈
    2. 如果栈为空,而且当前字符为右括号,返回False
    3. 如果栈不为空,而且栈顶字符正好是和当前字符(右括号)匹配的左括号,将此栈顶字符POP掉,如果不匹配返回False
* 循环完成后,如果栈为空,则全匹配返回True,否则返回False
"""
