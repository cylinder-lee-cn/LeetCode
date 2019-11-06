"""
925. 长按键入

你的朋友正在使用键盘输入他的名字 name。偶尔，在键入字符 c 时，按键可能会被长按，而字符可能被输入 1 次或多次。
你将会检查键盘输入的字符 typed。如果它对应的可能是你的朋友的名字（其中一些字符可能被长按），那么就返回 True。

示例 1：
输入：name = "alex", typed = "aaleex"
输出：true
解释：'alex' 中的 'a' 和 'e' 被长按。

示例 2：
输入：name = "saeed", typed = "ssaaedd"
输出：false
解释：'e' 一定需要被键入两次，但在 typed 的输出中不是这样。

示例 3：
输入：name = "leelee", typed = "lleeelee"
输出：true

示例 4：
输入：name = "laiden", typed = "laiden"
输出：true

解释：长按名字中的字符并不是必要的。
提示：
name.length <= 1000
typed.length <= 1000
name 和 typed 的字符都是小写字母。
"""


class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        while name:
            n = name[0]
            if (len(typed) - len(typed.lstrip(n)) >=
                    len(name) - len(name.lstrip(n))):
                typed = typed.lstrip(n)
                name = name.lstrip(n)
            else:
                return False
        return True


s = Solution()
print(s.isLongPressedName('alex', 'aaleex'))
print(s.isLongPressedName('saeed', 'ssaaedd'))
print(s.isLongPressedName('leelee', 'lleeelee'))
print(s.isLongPressedName('laiden', 'laiden'))
print(s.isLongPressedName('kikcxmvzi', 'kiikcxxmmvvzz'))

"""
此题解法：
* 要注意，name中的字符出现的顺序和在typed中出现的顺序一致。
* 而且，typed相同顺序出现的字符数量要>=name中对应顺序出现的字符数量，这样就是True，反之False
* 如果能使用python内置的groupy将name分组，程序会更简单。
* 遍历name，取最左边一个，然后同时对name和typed进行lstrip(n)，比较缩小的长度。typed缩小的长度应该>=
name缩小的长度。
"""
