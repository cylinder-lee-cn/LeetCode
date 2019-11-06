"""
14. 最长公共前缀
题目描述提示帮助提交记录社区讨论阅读解答
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
"""


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        words = len(strs)

        prefix = set()

        commonprefix = ""

        j = 0
        p = ""

        if words < 1:
            return ""
        if words == 1:
            return strs[0]

        while True:
            prefix.clear()
            for i in range(words):
                try:
                    p = strs[i][j]
                except:
                    #p = '0'
                    return commonprefix
                prefix.add(p)
            j = j + 1

            if len(prefix) == 1:
                commonprefix = commonprefix + p
            else:
                return commonprefix


S = Solution()
print(S.longestCommonPrefix(["",""]))

"""
解法:使用Python中Set的键值唯一的特性来解决.
* 如果空字符串就返回""
* 如果只有一个字符,就返回这个字符
* 取每一个单词的第j个字母,将其加入Set中,如果Set中的Key数量是1,那这个字母就是所有单词共有的.反之就可以返回
* 如果取到某个单词索引越界,证明这个单词的所有字母已经取完,程序无需继续,可以返回.
"""