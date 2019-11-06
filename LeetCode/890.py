"""
890. 查找和替换模式


你有一个单词列表 words 和一个模式  pattern，你想知道 words 中的哪些单词与模式匹配。

如果存在字母的排列 p ，使得将模式中的每个字母 x 替换为 p(x) 之后，我们就得到了所需的单词，那么单词与模式是匹配的。

（回想一下，字母的排列是从字母到字母的双射：每个字母映射到另一个字母，没有两个字母映射到同一个字母。）

返回 words 中与给定模式匹配的单词列表。

你可以按任何顺序返回答案。

示例：

输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
输出：["mee","aqq"]
解释：
"mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
"ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
因为 a 和 b 映射到同一个字母。


提示：
1 <= words.length <= 50
1 <= pattern.length = words[i].length <= 20
"""


class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

        pl_a = len(pattern)
        pl_b = len(set(pattern))

        result = []
        for w in words:
            w_a = len(w)
            w_b = len(set(w))
            if (w_a == pl_a and w_b == pl_b):
                party = set()
                for i in range(pl_a):
                    party.add((pattern[i], w[i]))

                if (len(party) == pl_b):
                    result.append(w)

        return result


s = Solution()
s.findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb")

"""
此题解法：
* 单词要满足pattern的模式，必须具备以下条件
1 单词长度与pattern长度相同，
2 单词中字母的个数（去重）与pattern字母的个数（去重）相同
3 同时遍历单词和pattern，相同位置字母对应关系的数量一定与去重后的字母个数相同

"""
