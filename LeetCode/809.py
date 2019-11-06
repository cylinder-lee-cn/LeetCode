"""
809. 情感丰富的文字

有时候人们会用额外的字母来表示额外的情感，比如 "hello" -> "heeellooo",
"hi" -> "hiii"。我们将连续的相同的字母分组，并且相邻组的字母都不相同。
我们将一个拥有三个或以上字母的组定义为扩张状态（extended），
如第一个例子中的 "e" 和" o" 以及第二个例子中的 "i"。
此外，"abbcccaaaa" 将有分组 "a" , "bb" , "ccc" , "dddd"；其中 "ccc" 和 "aaaa" 处于扩张状态。

对于一个给定的字符串 S ，如果另一个单词能够通过将一些字母组扩张从而使其和 S 相同，
我们将这个单词定义为可扩张的（stretchy）。我们允许选择一个字母组（如包含字母 c ），
然后往其中添加相同的字母 c 使其长度达到 3 或以上。注意，我们不能将一个只包含一个字母的字母组，
如 "h"，扩张到一个包含两个字母的组，如 "hh"；所有的扩张必须使该字母组变成扩张状态（至少包含三个字母）。

输入一组单词，输出其中可扩张的单词数量。

示例：
输入：
S = "heeellooo"
words = ["hello", "hi", "helo"]
输出：1

解释：
我们能通过扩张"hello"的"e"和"o"来得到"heeellooo"。
我们不能通过扩张"helo"来得到"heeellooo"因为"ll"不处于扩张状态。

说明：
0 <= len(S) <= 100。
0 <= len(words) <= 100。
0 <= len(words[i]) <= 100。
S 和所有在 words 中的单词都只由小写字母组成。
"""


class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """

        def wlist(string):
            temp = []
            count = 1
            s_l = len(string)
            if (s_l == 0):
                return [['', 0]]

            for i in range(s_l - 1):
                if (string[i] == string[i + 1]):
                    count = count + 1
                else:
                    temp.append([string[i], count])
                    count = 1
            temp.append([string[-1], count])
            return temp

        st = wlist(S)
        st_l = len(st)
        # print(st)

        result = 0

        for j, w in enumerate(words):
            wt = wlist(w)
            if (len(wt) == st_l):
                wcount = 0
                for k in range(st_l):
                    if (st[k][0] == wt[k][0]):
                        if (st[k][1] == wt[k][1]):
                            wcount = wcount + 1
                        elif (st[k][1] > wt[k][1] and st[k][1] >= 3):
                            wcount = wcount + 1
                        else:
                            continue
                if (wcount == st_l):
                    result = result + 1

        return result


s = Solution()
# s.expressiveWords('heeellooo', ["hello", "hi", "helo"])
# s.expressiveWords('hhhhhhello', ["hello", "hi", "helo"])
print(
    s.expressiveWords("dddiiiinnssssssoooo", [
        "dinnssoo", "ddinso", "ddiinnso", "ddiinnssoo", "ddiinso", "dinsoo",
        "ddiinsso", "dinssoo", "dinso"
    ]))
"""
此题解法：
* 首先将S按照顺序进行相同字母的统计，heeellooo就统计成 [h,1][e,3][l,2][o,3] 的st
* 遍历words，将每个单词按照同样的方法整理成 [字母,计数]的列表wt
* 如果wt和st的长度相同，再进一步依次比较每个元素
* 首先必须字母相同，在字母相同的条件下：
    1. 要么计数相同，表示wt[k]和st[k]满足条件
    2. 如果st[k]的计数也就是st[k][1]>wt[k][1]，还必须>=3，也满足条件
    3. 如果st和wt都满足以上条件，那么计数+1
"""
