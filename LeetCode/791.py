"""
791. 自定义字符串排序

字符串S和 T 只包含小写字符。在S中，所有字符只会出现一次。

S 已经根据某种规则进行了排序。我们要根据S中的字符顺序对T进行排序。
更具体地说，如果S中x在y之前出现，那么返回的字符串中x也应出现在y之前。

返回任意一种符合条件的字符串T。

示例:
输入:
S = "cba"
T = "abcd"
输出: "cbad"
解释:
S中出现了字符 "a", "b", "c", 所以 "a", "b", "c" 的顺序应该是 "c", "b", "a".
由于 "d" 没有在S中出现, 它可以放在T的任意位置. "dcba", "cdba", "cbda" 都是合法的输出。
注意:

S的最大长度为26，其中没有重复的字符。
T的最大长度为200。
S和T只包含小写字符。
"""


class Solution:
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        az = 'abcdefghijklmnopqrstuvwxyz'
        sl = list(S)
        sl.extend([c for c in az if c not in sl])
        result = []

        td = {}
        for t in T:
            td[t] = td.get(t, 0) + 1

        for s in sl:
            if (s in td):
                result.append(s * td[s])
        return ''.join(result)


s = Solution()
s.customSortString('cba', 'abcd')
"""
此题解法：
* 由于S最多也是26个字母，所以将S转换成List，然后在后面补上之前没有出现在S中的字母，就成了一个完整26个字母的自定义序
* 遍历T，统计字母和出现的次数
* 按照定义序sl，对比td中的元素，这就可以按照自定义的字典序输出：字母*次数

"""
