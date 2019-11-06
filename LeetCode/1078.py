"""
1078. Bigram 分词

给出第一个词 first 和第二个词 second，考虑在某些文本 text 中可能以 "first second third" 形式出现的情况，
其中 second 紧随 first 出现，third 紧随 second 出现。

对于每种这样的情况，将第三个词 "third" 添加到答案中，并返回答案。

示例 1：
输入:text = "alice is a good girl she is a good student",first="a",second="good"
输出:["girl","student"]

示例 2：
输入：text = "we will we will rock you", first = "we", second = "will"
输出：["we","rock"]

提示：
1 <= text.length <= 1000
text 由一些用空格分隔的单词组成，每个单词都由小写英文字母组成
1 <= first.length, second.length <= 10
first 和 second 由小写英文字母组成
"""

from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        textList = text.split(' ')

        tl = len(textList)

        idx = 0

        result = []

        while idx < tl-2:
            if textList[idx] == first and textList[idx + 1] == second:
                result.append(textList[idx + 2])
                idx = idx + 2
            else:
                idx = idx + 1
        # print(result)
        return result


s = Solution()
s.findOcurrences(text="alice is a good girl she is a good student",
                 first="a",
                 second="good")

s.findOcurrences("we will we will rock you", "we", "will")
s.findOcurrences(
    "jkypmsxd jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa jkypmsxd kcyxdfnoa kcyxdfnoa jkypmsxd kcyxdfnoa",
    "kcyxdfnoa", "jkypmsxd")

"""
此题解法：
* 首先使用split将字符串拆成List
* 计算list长度，然后用索引来进行访问
* 用while循环，为了保证索引不越界（因为匹配的话需要访问到当前索引后面连续2个），长度-2
* 然后分别比较当前index和index+1是否与first和second相同，如果相同那就将index+2放入结果，index向后跳2
* 反之index向后跳1
"""
