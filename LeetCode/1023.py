"""
1023. 驼峰式匹配

如果我们可以将小写字母插入模式串 pattern 得到待查询项 query，那么待查询项与给定模式串匹配。
（我们可以在任何位置插入每个字符，也可以插入 0 个字符。）

给定待查询列表 queries，和模式串 pattern，返回由布尔值组成的答案列表 answer。
只有在待查项 queries[i] 与模式串 pattern 匹配时， answer[i] 才为 true，否则为 false。

示例 1：
输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
输出：[true,false,true,true,false]
示例：
"FooBar" 可以这样生成："F" + "oo" + "B" + "ar"。
"FootBall" 可以这样生成："F" + "oot" + "B" + "all".
"FrameBuffer" 可以这样生成："F" + "rame" + "B" + "uffer".

示例 2：
输入：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBa"
输出：[true,false,true,false,false]
解释：
"FooBar" 可以这样生成："Fo" + "o" + "Ba" + "r".
"FootBall" 可以这样生成："Fo" + "ot" + "Ba" + "ll".

示例 3：
输出：queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FoBaT"
输入：[false,true,false,false,false]
解释：
"FooBarTest" 可以这样生成："Fo" + "o" + "Ba" + "r" + "T" + "est".

提示：
1 <= queries.length <= 100
1 <= queries[i].length <= 100
1 <= pattern.length <= 100
所有字符串都仅由大写和小写英文字母组成。
"""


class Solution(object):
    def camelMatch(self, queries, pattern):
        """
        :type queries: List[str]
        :type pattern: str
        :rtype: List[bool]
        """
        import collections

        capital = {
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
        }

        finalResult = []

        def cutAsCaptial(words):
            tmp = words[0]
            result = []
            for w in words[1:]:
                if w in capital:
                    result.append(tmp)
                    tmp = w
                else:
                    tmp = tmp + w
            result.append(tmp)
            return result

        def matchPattern(pparts, wparts):
            # print(wparts)
            if len(pparts) == len(wparts):
                # return all(
                #     [i[1].startswith(i[0]) for i in zip(pparts, wparts)])
                for i, v in enumerate(pparts):
                    pdict = collections.Counter(v)
                    wdict = collections.Counter(wparts[i])
                    if all(pdict[k] == wdict[k] for k in pdict.keys()):
                        return True
                    else:
                        return False
            return False

        patternParts = cutAsCaptial(pattern)
        # print(patternParts)

        for q in queries:
            finalResult.append(matchPattern(patternParts, cutAsCaptial(q)))

        return finalResult


s = Solution()
print(
    s.camelMatch(
        ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
        "FB"))
print(
    s.camelMatch(
        ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
        "FoBa"))
print(
    s.camelMatch(
        ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"],
        "FoBaT"))
print(
    s.camelMatch(["CompetitiveProgramming", "CounterPick", "ControlPanel"],
                 "CooP"))
"""
此题解法：
* 首先要将pattern用大写字母作为间隔拆开
* 其次要将queries的每个单词都用大写字母作为间隔拆开
* 然后将queries单词拆开后的结果和pattern的结果进行比较
  * 首先比较长度，必须长度相同
  * 其次是每个元素的第一个字母相同
  * q中每个元素的小写字母，在对应的w中都能对应，数量相同
  * Todo。。。。。
"""
